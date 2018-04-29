import os
import tornado.ioloop
import tornado.web
from tornado.options import parse_command_line

STATIC_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                           'client/build/static'))

CLIENT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                           'client'))

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        with open(os.path.join(CLIENT_PATH, 'build/index.html')) as f:
            self.write(f.read())


def make_app():
    return tornado.web.Application([
        (r'/', MainHandler),
        (r'/static/(.*)', tornado.web.StaticFileHandler,
         {'path': STATIC_PATH}),
    ])


if __name__ == '__main__':
    parse_command_line()
    app = make_app()
    port = int(os.environ.get('PORT', 5000))
    app.listen(port)
    tornado.ioloop.IOLoop.current().start()
