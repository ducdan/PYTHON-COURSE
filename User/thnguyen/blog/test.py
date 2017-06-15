import unittest
from flask_testing import TestCase
from blog.blogful import app,db,User, Entry

class BaseTestCase(TestCase):
    def create_app(self):
        app.config.from_object('config.TestConfig')
        return app

    def setUp(self):
        db.create_all()
        db.session.add_all([User("admin", "admin@blog", "123"), Entry("title1","content1")])
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        
class FlaskTestCase(BaseTestCase):

    # # Ensure to require user login
    def test_requires_login(self):
        response1 = self.client.get('/', follow_redirects=True)
        response2 = self.client.get('/add', follow_redirects=True)
        response3 = self.client.get('/entry/1', follow_redirects=True)
        response4 = self.client.get('/entry/1/edit', follow_redirects=True)
        response5 = self.client.get('/entry/1/delete', follow_redirects=True)
        
        self.assertIn(b'method="post"', response1.data)
        self.assertIn(b'login', response1.data)
        self.assertIn(b'login', response2.data)
        self.assertIn(b'login', response3.data)
        self.assertIn(b'login', response4.data)
        self.assertIn(b'login', response5.data)


    def test_add(self):
        self.test_correct_login()
        response = self.client.post(
            '/add',
            data=dict(title="It is a title", content="the content here."),
            follow_redirects=True
        )
        latest_entry = Entry.query.filter().order_by(Entry.datetime.desc()).first()
        self.assertTrue(latest_entry.title == "It is a title")
        self.assertTrue(latest_entry.content == "the content here.")
        self.assertIn("It is a title", response.data.decode())
        
    def test_edit(self):
        self.test_correct_login()
        response = self.client.post(
            '/entry/1/edit',
            data=dict(title="New title", content="I change 1st entry to new content"),
            follow_redirects=True
        )

        edited = Entry.query.filter_by(id=1).first()
        self.assertEqual(edited.title, "New title")
        self.assertEqual(edited.content, "I change 1st entry to new content")
        self.assertIn("I change 1st entry to new content", str(response.data))
        self.assertIn('View all entries', str(response.data))
         
        
    def test_view(self):
        self.test_correct_login()
        response = self.client.get(
            'entry/1',
            content_type='html/text'
            )
        print (response.data)
        self.assertIn('title1', str(response.data))
        self.assertIn('content1', str(response.data))
        self.assertIn('View all entries', str(response.data))

    
    def test_delete(self):
        self.test_correct_login()
        response = self.client.get(
            '/entry/1/delete',
            follow_redirects=True
        )
        self.assertEqual(Entry.query.filter_by(id=1).first(), None)
        self.assertIn('reload', str(response.data))

    def test_correct_login(self):
        response = self.client.post(
            '/login',
            data=dict(username="admin", password="123"),
            follow_redirects=True
        )
        self.assertEquals(response.status_code,200)
        self.assertIn('Add New Post', str(response.data))

    def test_incorrect_login(self):
        response = self.client.post(
            '/login',
            data=dict(username="user1", password="1"),
            follow_redirects=True
        )
        self.assertEquals(response.status_code,200)
        self.assertIn('Login', str(response.data))
     
if __name__ == '__main__':
    unittest.main()