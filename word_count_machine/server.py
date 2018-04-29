import os
import tornado.ioloop
import tornado.web
from tornado.options import parse_command_line


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('Hello, world')


def make_app():
    return tornado.web.Application([
        (r'/', MainHandler),
    ])


if __name__ == '__main__':
    parse_command_line()
    app = make_app()
    port = int(os.environ.get('PORT', 5000))
    app.listen(port)
    tornado.ioloop.IOLoop.current().start()
