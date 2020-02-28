import tornado.ioloop
import tornado.web

from MainHandler import MainHandler
from GameHandler import GameHandler

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
	    (r"/game(?:/([a-zA-Z0-9]*))?", GameHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
