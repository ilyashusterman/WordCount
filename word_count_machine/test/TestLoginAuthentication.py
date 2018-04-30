from unittest import TestCase

from word_count_machine.LoginAuthentication import LoginAuthentication


class TestLoginAuthentication(TestCase):

    def setUp(self):
        self.login_auth = LoginAuthentication()

    def test_user_auth(self):
        result = self.login_auth.authenticate('ilya', 'password')
        self.assertTrue(result)

    def test_bad_user_auth(self):
        result = self.login_auth.authenticate('ilya', 'password1qeqweqwe')
        self.assertFalse(result)