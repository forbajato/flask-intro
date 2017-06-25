# tests/test_functional.py

import unittest

from flask_login import current_user

from base import BaseTestCase


class FlaskTestCase(BaseTestCase):

    # Ensure that Flask was set up correctly
    def test_index(self):
        response = self.client.get('/login', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # Ensure the main page requires a login
    def test_main_route_requires_login(self):
        response = self.client.get('/', follow_redirects=True)
        self.assertTrue(b'Please log in to access this page.' in response.data)

    # Ensure welcome route works as expected
    def test_welcome_route_works_as_expected(self):
        response = self.client.get('/welcome', follow_redirects=True)
        self.assertTrue(b'Welcome to Flask!' in response.data)

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
            response = self.client.get('/logout', follow_redirects=True)
            self.assertIn(b'You were just logged out', response.data)
            # Flask-Login > 0.3 treats is_active as a property not a method
            self.assertFalse(current_user.is_active)

    # Ensure the logout page requires a login
    # NB: the flask-login code returns the string "Please log in to access this page." as its not logged in message.
    def test_logout_route_requires_login(self):
        response = self.client.get('/logout', follow_redirects=True)
        self.assertTrue(b'Please log in to access this page.' in response.data)


if __name__ == '__main__':
    unittest.main()
