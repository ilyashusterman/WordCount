import os
from secrets import token_urlsafe

import tornado.ioloop
import tornado.web
from tornado.options import parse_command_line

from word_count_machine.LoginAuthentication import LoginAuthentication
from word_count_machine.WordCounter import WordCounter

STATIC_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                           'client/build/static'))

CLIENT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                           'client'))

class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("user")

class WordCounterHandler(BaseHandler):

    def initialize(self, word_counter):
        super(WordCounterHandler, self).initialize()
        self.word_counter = word_counter

    def post(self):
        if not self.current_user:
            return
        else:
            counts = self.word_counter.get_words_count_url(words, url)


class MainHandler(BaseHandler):
    def get(self):
        with open(os.path.join(CLIENT_PATH, 'build/index.html')) as f:
            self.write(f.read())

class LoginHandler(BaseHandler):

    def initialize(self, login_auth):
        super(LoginHandler, self).initialize()
        self.login_auth = login_auth

    def post(self):
        if self.login_auth.authenticate(username, password):
            self.set_secure_cookie("user", self.get_argument("name"))


def make_app():
    settings = {
        'cookie_secret': token_urlsafe(32),
    }
    login_auth = dict(login_auth=LoginAuthentication())
    word_counter = dict(word_counter=WordCounter())
    return tornado.web.Application([
        (r'/', MainHandler),
        (r'/count', WordCounterHandler, word_counter),
        (r'/login', LoginHandler, login_auth),
        (r'/static/(.*)', tornado.web.StaticFileHandler,
         {'path': STATIC_PATH}),
    ], **settings)


if __name__ == '__main__':
    parse_command_line()
    app = make_app()
    port = int(os.environ.get('PORT', 5000))
    app.listen(port)
    tornado.ioloop.IOLoop.current().start()
