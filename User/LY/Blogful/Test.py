import unittest
from flask_testing import TestCase
from Blogful import app,db,User, login_user, current_user

class BaseTestCase(TestCase):
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

class RegisterProgressing(BaseTestCase):
    # Ensure that Flask was set up correctly
    def test_register(self):
        with self.app.test_client() as client:
            response = self.client.get('/register', content_type='html/text')
            self.assert200(response)
            self.assertIn(b'Register', response.data)
            self.assertTemplateUsed('add-user.html')

    # Test user overlap when registering
    def test_register_user(self):
        response_1 = self.client.post(
            '/register',
            data=dict(username = 'LY1',password = '123',email = 'ly1@gmail.com'),
            follow_redirects=True)

        response_2 = self.client.post(
            '/register',
            data=dict(username = 'LY1',password = '456',email = 'ly2@gmail.com'),
            follow_redirects=True)

        self.assert200(response_1)
        user = User.query.filter_by(name='LY1').first()
        self.assertIsNotNone(user)
        self.assertIn(b'Choose another name',response_2.data)
        # print(response.__dict__)
        # print(vars(response))

class LogInOutProcessing(BaseTestCase):
    # Ensure that main page requires user login
    def test_main_route_requires_login(self):
        response = self.client.get('/page/1', follow_redirects=True)
        self.assert404(response)

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
        self.assertNotIn(b'<title>Log in</title>', response.data)

    def test_logout_authenticated(self):
        user = self.client.post(
            '/login',
            data=dict(username='admin', password='admin', email='admin@gmail.com'),
            follow_redirects=True)
        response = self.client.get('/logout', content_type='html/text')
        self.assert200(response)
        self.assertTemplateUsed('logout.html')
        self.assertIn(b'<title>Logout page</title>', response.data)

    def test_logout_unauthenticated(self):
        response = self.client.get('/logout', content_type='html/text')
        self.assertRedirects(response,'login')

class EntryProcessing(BaseTestCase):
    # Test everything about entries

    def test_add_entry_isAuthenticated(self):
        response = self.client.get('/entries/add', content_type='html/text')
        self.assertRedirects(response, 'login')

    def test_view_entry_isAuthenticated(self):
        response = self.client.get('/entries/1', content_type='html/text')
        self.assertRedirects(response, 'login')

    def test_edit_entry_isAuthenticated(self):
        response = self.client.get('/entries/1/edit', content_type='html/text')
        self.assertRedirects(response, 'login')

    def test_delete_entry_isAuthenticated(self):
        response = self.client.get('/entries/1/delete', content_type='html/text')
        self.assertRedirects(response, 'login')

    def test_entry(self):
        # Add user for authentication
        response = self.client.post(
            '/login',
            data=dict(username="admin", password="admin"),
            follow_redirects=True
        )
        self.assert200(response)
        self.assertIn(b'<title>Main page</title>', response.data)
        self.assertNotIn(b'Entry Test', response.data)

        # Making a new post for testing
        newpost = self.client.post(
            '/entries/add',
            data=dict(title="Entry Test", content="abcdefghijklmnopqrst123456789"),
            follow_redirects=True)
        self.assert200(newpost)
        self.assertIn(b'<title>Main page</title>', newpost.data)
        self.assertIn(b'Entry Test', newpost.data)
        self.assertIn(b'abcdefghijklmnopqrst123456789', newpost.data)

        # Viewing post
        viewed_post = self.client.post('/entries/1', content_type='html/text')
        self.assert200(viewed_post)
        self.assertIn(b'<title>View entry</title>', viewed_post.data)
        self.assertIn(b'Entry Test', viewed_post.data)
        self.assertIn(b'abcdefghijklmnopqrst123456789', viewed_post.data)

        # Editing post
        edited_post = self.client.post(
            '/entries/1/edit',
            data=dict(title="Edited", content="987654321tsrqponmlkjihgfedcba"),
            follow_redirects=True)
        self.assert200(edited_post)
        self.assertIn(b'<title>View entry</title>', edited_post.data)
        self.assertNotIn(b'Entry Test', edited_post.data)
        self.assertNotIn(b'abcdefghijklmnopqrst123456789', edited_post.data)
        self.assertIn(b'Edited', edited_post.data)
        self.assertIn(b'987654321tsrqponmlkjihgfedcba', edited_post.data)

        # Deleting post with cancel button
        undeleted_post = self.client.post(
            '/entries/1/delete',
            data=dict(title="", content="",submit='cancel'),
            follow_redirects=True)
        self.assert200(undeleted_post)
        self.assertIn(b'<title>View entry</title>', undeleted_post.data)
        self.assertIn(b'Edited', undeleted_post.data)
        self.assertIn(b'987654321tsrqponmlkjihgfedcba', undeleted_post.data)

        # Deleting post with delete button
        deleted_post = self.client.post(
            '/entries/1/delete',
            data=dict(title="", content="", submit='delete'),
            follow_redirects=True)
        self.assert200(deleted_post)
        self.assertIn(b'<title>Main page</title>', deleted_post.data)
        self.assertNotIn(b'Edited', deleted_post.data)
        self.assertNotIn(b'987654321tsrqponmlkjihgfedcba', deleted_post.data)

if __name__ == '__main__':
    unittest.main()