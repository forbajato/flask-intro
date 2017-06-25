# tests/test_basic.py

import unittest

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


if __name__ == '__main__':
    unittest.main()
