import unittest
from flask_testing import TestCase
from flask_login import current_user
from project import app, db
from project.models import User, BlogPost


class BaseTestCase(TestCase):
    """ A Base test case """

    def create_app(self):
        app.config.from_object('config.TestConfig')
        return app

    def setUp(self):
        db.create_all()
        db.session.add(User("admin", "ad@min.com", "admin"))
        db.session.add(BlogPost("Test post",
                                "This is a test. Only a test.", "admin"))
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


class FlaskTestCase(BaseTestCase):

    # Ensure that Flask was set up correctly
    def test_index(self):
        response = self.client.get('/login', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # Ensure the main page requires a login
    def test_main_route_requires_login(self):
        response = self.client.get('/', follow_redirects=True)
        self.assertTrue(b'Please log in to access this page.' in response.data)

    # Ensure that posts show up on the main page
    def test_post_show_up(self):
        response = self.client.post(
            '/login',
            data=dict(username="admin", password="admin"),
            follow_redirects=True)
        self.assertIn(b'Test post', response.data)


class UsersViewsTests(BaseTestCase):

    # Ensure that login page loads correctly
    def test_login_page_loads(self):
        response = self.client.get('/login', content_type='html/text')
        self.assertTrue(b'Please login' in response.data)

    # Ensure that login behaves correctly with correct credentials
    def test_correct_login(self):
        with self.client:
            response = self.client.post(
                '/login',
                data=dict(username="admin", password="admin"),
                follow_redirects=True)
            self.assertIn(b'You were just logged in', response.data)
            self.assertTrue(current_user.name == "admin")
            self.assertTrue(current_user.is_active)

    # Ensure that login behaves correctly with incorrect credentials
    def test_incorrect_login(self):
        response = self.client.post(
            '/login',
            data=dict(username="tom", password="tom"),
            follow_redirects=True)
        self.assertIn(b'Invalid credentials. Please try again.', response.data)

    # Ensure that logout behaves correctly
    def test_logout(self):
        with self.client:
            self.client.post(
                '/login',
                data=dict(username="admin", password="admin"),
                follow_redirects=True
            )
            response = self.client.get('/logout',follow_redirects=True)
            self.assertIn(b'You were just logged out', response.data)
            # Flask-Login > 0.3 treats is_active as a property not a method
            self.assertFalse(current_user.is_active)

    # Ensure the logout page requires a login
    # NB: the flask-login code returns the string "Please log in to access this page." as its not logged in message.
    def test_logout_route_requires_login(self):
        response = self.client.get('/logout', follow_redirects=True)
        self.assertTrue(b'Please log in to access this page.' in response.data)

    # Ensure user can register
    def test_user_registration(self):
        with self.client:
            response = self.client.post(
                '/register',
                data=dict(username="Rebekah", email="skate@liberty.com",
                          password="skater", confirm="skater"),
                follow_redirects=True)
            self.assertIn(b'Welcome to Flask!', response.data)
            self.assertTrue(current_user.name == "Rebekah")
            self.assertTrue(current_user.is_active)


if __name__ == '__main__':
    unittest.main()
