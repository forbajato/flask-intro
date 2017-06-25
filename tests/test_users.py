# tests/test_users.py

import unittest

from flask_login import current_user
from flask import request

from base import BaseTestCase
from project import bcrypt
from project.models import User


class TestUser(BaseTestCase):

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
            user = User.query.filter_by(email='skate@liberty.com').first()
            self.assertTrue(str(user) == '<name: Rebekah>')

    def test_incorrect_user_registration(self):
        with self.client:
            response = self.client.post('/register', data=dict(
                       username='Michael', email='michael',
                       password='python', confirm='python'
            ), follow_redirects=True)
            self.assertIn(b'Invalid email address', response.data)
            self.assertIn('/register', request.url)

    def test_get_by_id(self):
        # Ensure id is correct for current logged in username
        with self.client:
            self.client.post('/login', data=dict(
                             username="admin", password="admin"
                             ), follow_redirects=True)
            self.assertTrue(current_user.id == 1)
            self.assertFalse(current_user.id == 20)

    def test_check_password(self):
        # Ensure password hashing is correct
        user = User.query.filter_by(email="ad@min.com").first()
        self.assertTrue(bcrypt.check_password_hash(user.password, 'admin'))
        self.assertFalse(bcrypt.check_password_hash(user.password, 'foobar'))


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
