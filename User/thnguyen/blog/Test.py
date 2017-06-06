import unittest
from flask_testing import TestCase
from blog.blogful import app,db,User, Entry
class BaseTestCase(TestCase):
    def create_app(self):
        app.config.from_object('config.TestConfig')
        return app

    def setUp(self):
        db.create_all()
        db.session.add(User("admin", "admin@blog", "123"),Entry("title1","content1"))
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
class FlaskTestCase(BaseTestCase):
    # Ensure that Flask was set up correctly
    def test_index(self):
        with self.app.test_client() as client:
            response = self.client.post('/add', content_type='html/text')
            print(response.data)
#             self.assertTrue(response.data==b'Registed successful')
            self.assertEqual(response.status_code, 200)
#             self.assertIn(b'successful',response.data)

    # # Ensure that main page requires user login
    def test_main_route_requires_login(self):
        response = self.client.get('/', follow_redirects=True)
        print(response.data)
        self.assertEquals(response.status_code,200)
        self.assertIn(b'method="post"', response.data)

    def test_login(self):
        response = self.client.post(
            '/login',
            data=dict(username="admin", password="123"),
            follow_redirects=True
        )
        print(response.data)
        self.assertEquals(response.status_code,200)
        self.assertIn('Add New Post', str(response.data))


if __name__ == '__main__':
    unittest.main()