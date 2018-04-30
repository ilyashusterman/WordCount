from tornado.testing import AsyncHTTPTestCase

from word_count_machine import server


class TestServer(AsyncHTTPTestCase):
    def get_app(self):
        return server.make_app()

    def test_server_login(self):
        pass