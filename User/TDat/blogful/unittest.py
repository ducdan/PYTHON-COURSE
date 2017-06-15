import unittest
from flask_testing import TestCase
from blogful import app,db,User

class Test(TestCase):
    def create_app(self):
        app.config.from_object('config.TestConfig')
        return app

    def setUp(self):
        db.create_all()
        db.session.add(User("admin", "admin@gmail.com", "admin"))
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestEntry(Test):

    def test_entry(self):

        response = self.client.post(
            '/login',
            data=dict(username="admin", password="admin"),
            follow_redirects=True
        )
        self.assert200(response)
        self.assertIn(b'<title>Main page</title>', response.data)
        self.assertNotIn(b'Entry Test', response.data)


        testpost = self.client.post(
            '/entries/add',
            data=dict(title="Entry Test", content="DangAnh"),
            follow_redirects=True)
        self.assert200(testpost)
        self.assertIn(b'<title>Main page</title>', testpost.data)
        self.assertIn(b'Entry Test', testpost.data)
        self.assertIn(b'DangAnh', testpost.data)

        # Viewing post
        viewed_post = self.client.post('/entries/1', content_type='html/text')
        self.assert200(viewed_post)
        self.assertIn(b'<title>View entry</title>', viewed_post.data)
        self.assertIn(b'Entry Test', viewed_post.data)
        self.assertIn(b'DangAnh', viewed_post.data)

        # Editing post
        edited_post = self.client.post(
            '/entries/1/edit',
            data=dict(title="Edited", content="tintin95"),
            follow_redirects=True)
        self.assert200(edited_post)
        self.assertIn(b'<title>View entry</title>', edited_post.data)
        self.assertNotIn(b'Entry Test', edited_post.data)
        self.assertNotIn(b'DangAnh', edited_post.data)
        self.assertIn(b'Edited', edited_post.data)
        self.assertIn(b'DangAnh', edited_post.data)

        # Deleting post with cancel button
        undeleted_post = self.client.post(
            '/entries/1/delete',
            data=dict(title="", content="",submit='cancel'),
            follow_redirects=True)
        self.assert200(undeleted_post)
        self.assertIn(b'<title>View entry</title>', undeleted_post.data)
        self.assertIn(b'Edited', undeleted_post.data)
        self.assertIn(b'DangAnh', undeleted_post.data)

        # Deleting post with delete button
        deleted_post = self.client.post(
            '/entries/1/delete',
            data=dict(title="", content="", submit='delete'),
            follow_redirects=True)
        self.assert200(deleted_post)
        self.assertIn(b'<title>Main page</title>', deleted_post.data)
        self.assertNotIn(b'Edited', deleted_post.data)
        self.assertNotIn(b'DangAnh', deleted_post.data)

class TestLogin(Test):


    def test_login_correct(self):
        response = self.client.post(
            '/login',
            data=dict(username="admin", password="admin"),
            follow_redirects=True
        )
        self.assert200(response)
        self.assertIn(b'<title>Main page</title>', response.data)

    def test_login_incorrect(self):
        response = self.client.post(
            '/login',
            data=dict(username="admin", password="wrongpass"),
            follow_redirects=True
        )
        self.assert200(response)
        self.assertNotIn(b'<title>Main page</title>', response.data)
        self.assertNotIn(b'<title>Elegant Login - Designscrazed</title>', response.data)



if __name__ == '__main__':
    unittest.main()


