import tornado.web
import json
from util.connectdb import Connectdb
from util.getselect import Get_select

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        # 首页
        self.render('index.html')