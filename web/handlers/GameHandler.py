import tornado.ioloop
import tornado.web

class GameHandler(tornado.web.RequestHandler):
    def get(self, token):
        if token == None:
            token = ''
        self.render("game.html", token=token)