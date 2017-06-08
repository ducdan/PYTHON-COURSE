import unittest
from flask_testing import TestCase
from Blogful import app, db, User, login_user, current_user

class BaseTestCase(TestCase):
    def create_app(self):
        app.config.from_object('config.TestConfig')
        return app

    def setUp(self):
        db.create_all()
        db.session.add(User('admin', '123@gmail.com', '123'))
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class LogInOutTestCase(BaseTestCase):
    def test_logInOut(self):
        # Correct login
        login_response1 = self.client.post(
            '/login',
            data = dict(username="admin", password='123'),
            follow_redirects = True
        )

        self.assert200(login_response1)
        self.assertIn(b'<title>Entries</title>', login_response1.data)

        # Logout
        logout_response = self.client.get(
            '/logout'
        )
        self.assert200(logout_response)
        self.assertIn(b'Logout success', logout_response.data)

        # Incorrect login when username is not exit
        login_response2 = self.client.post(
            '/login',
            data=dict(username="user", password='123'),
            follow_redirects=True
        )

        self.assert200(login_response2)
        self.assertIn(b'Username is not exit', login_response2.data)

        # Incorrect login when password is wrong
        login_response3 = self.client.post(
            '/login',
            data=dict(username="admin", password='123456'),
            follow_redirects=True
        )

        self.assert200(login_response3)
        self.assertIn(b'Password is wrong', login_response3.data)



class EntryTestCase(BaseTestCase):
    def test_Entry(self):
        # Login for authentication
        login_response = self.client.post(
            '/login',
            data = dict(username = "admin", password = "123"),
            follow_redirects = True
        )
        self.assert200(login_response)
        self.assertIn(b'<title>Entries</title>', login_response.data)

        # Add entry
        add_response = self.client.post(
            'entry/add',
            data = dict(title='Entry test', content='testing testing testing testing testing testing testing'),
            follow_redirects = False
        )
        self.assert200(add_response)
        self.assertIn(b'<title>View Entry</title>', add_response.data)
        self.assertIn(b'Entry test', add_response.data)
        self.assertIn(b'testing testing testing testing testing testing testing', add_response.data)


        # Edit entry
        edit_response1 = self.client.post(
            'entry/1/edit',
            data = dict(title="Test 1", content="hello hello hello hello"),
            follow_redirects = False
        )
        self.assert200(edit_response1)
        self.assertIn(b'<title>View Entry</title>', edit_response1.data)
        self.assertIn(b'Test 1', edit_response1.data)
        self.assertNotIn(b'Entry test', edit_response1.data)
        self.assertIn(b'hello', edit_response1.data)
        self.assertNotIn(b'testing', edit_response1.data)

        edit_response2 = self.client.post(
            'entry/2/edit',
            data=dict(title="Test 2", content="abc abc abc"),
            follow_redirects=False
        )
        self.assert200(edit_response2)
        self.assertIn(b'Id is not exit to edit!', edit_response2.data)

        # View entry
        view_response1 = self.client.get(
            'entry/1',
            content_type='html/text'
        )
        self.assert200(view_response1)
        self.assertIn(b'<title>View Entry</title>', view_response1.data)
        self.assertIn(b'Test 1', view_response1.data)
        self.assertIn(b'hello', view_response1.data)

        view_response2 = self.client.get(
            'entry/2',
            follow_redirects=False,
            content_type='html/text'
        )
        self.assert200(view_response2)
        self.assertIn(b'Id is not exit to view!', view_response2.data)

        # Delete entry
        delete_response1 = self.client.get(
            'entry/1/delete',
            follow_redirects=True
        )
        self.assert200(delete_response1)
        self.assertNotIn(b'Test 1', delete_response1.data)

        delete_response2 = self.client.get(
            'entry/1/delete',
            follow_redirects=False,
            content_type='html/text'
        )
        self.assert200(delete_response2)
        self.assertIn(b'Id is not exit to delete!', delete_response2.data)


if __name__ == '__main__':
    unittest.main()