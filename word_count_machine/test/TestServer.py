import json

from tornado.testing import AsyncHTTPTestCase

from word_count_machine import server


class TestServer(AsyncHTTPTestCase):
    def get_app(self):
        return server.make_app()

    def test_server_login(self):
        body = {'username': 'ilya',
                'password': 'password'}
        response = self.fetch('/login', body=json.dumps(body), method='POST')
        response_body = json.loads(response.body)
        self.assertDictEqual(response_body, {'status': 'ok'})