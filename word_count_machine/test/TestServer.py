import json
from time import sleep
from unittest import mock

from tornado.testing import AsyncHTTPTestCase

from word_count_machine import server
from word_count_machine.server import LoginHandler, WordCounterHandler


class TestServer(AsyncHTTPTestCase):
    def get_app(self):
        return server.make_app()

    def test_server_login(self):
        body = {'username': 'ilya',
                'password': 'password'}
        self.check_login(body, {'status': 'ok'})

    def test_server_false_login(self):
        body = {'username': 'ilya',
                'password': 'password2'}
        response_result = {'reason': 'wrong credentials'}
        self.check_login(body, response_result)

    def check_login(self, body, response_result):
        response = self.fetch('/login', body=json.dumps(body), method='POST')
        response_body = json.loads(response.body)
        self.assertDictEqual(response_body, response_result)

    def test_words_count(self):
        self.check_login({'username': 'ilya',
                'password': 'password'}, {'status': 'ok'})
        sleep(3)
        body = {
            'words': ['chart'],
            'url': 'http://www.chartjs.org/'
        }
        with mock.patch.object(WordCounterHandler, 'get_secure_cookie') as m:
            m.return_value = 'user'
            response = self.fetch('/count', body=json.dumps(body),
                                  method='POST')
            response_body = json.loads(response.body)
            self.assertDictEqual(response_body, {'chart': 7})