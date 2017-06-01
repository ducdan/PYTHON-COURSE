import unittest
from _md5 import md5

from flask_testing import TestCase
from Login_Tutorial import app,db,User,current_user,json

class BaseTestCase(TestCase):
    def create_app(self):
        app.config.from_object('config.TestConfig')
        return app

    def setUp(self):
        db.create_all()
        db.session.add(User("admin2", "1234567"))
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
class FlaskTestCase(BaseTestCase):
    # Ensure that Flask was set up correctly
    def test_index(self):
        with self.app.test_client() as client:
            response = self.client.post(
                '/register',
                data=dict(username="admin", password="123456"),
                follow_redirects=True
            )
            user=User.query.filter_by(user_name='admin').first()
            self.assertTrue(user.id==2)
            # print(response.data)
            self.assertTrue(response.data==b'Registed successful')
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'successful',response.data)

    # # Ensure that main page requires user login
    def test_main_route_requires_login(self):
        response = self.client.get('/', follow_redirects=True)
        print(response.data)
        self.assertEquals(response.status_code,200)
        self.assertIn(b'', response.data)

    def test_login(self):
        response = self.client.post(
            '/login',
            data=dict(username="admin3", password="1234567"),
            follow_redirects=True
        )
        print(response.data)
        self.assertEquals(response.status_code,200)
        self.assertIn('Đăng nhập'.encode(), response.data)

    def test_getUser_api(self):
        with self.app.test_client() as client:
            response = self.client.get(
                '/api/admin2/1234567',
                follow_redirects=True,content_type='application/json'
            )
            print(response.data)
            self.assertEquals(response.status_code,200)
            self.assertEquals(response.data.decode('utf-8'),md5('1234567'.encode()).hexdigest())
            # print()
            # self.assertTrue(md5('1234567'.encode()).hexdigest().(response.data))
        # self.assertIn(b'admin', response.data)

if __name__ == '__main__':
    unittest.main()