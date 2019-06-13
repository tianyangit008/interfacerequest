import tornado.web
import os
import json
import tornado.httpserver
import tornado.options
import tornado.ioloop
from tornado.options import define,options
from util.connectdb import Connectdb
from util.getselect import Get_select
from index import IndexHandler
from getdomainhandler import GetDomainHandler
from getinterfaceshandler import GetInterfacesHandler

define(name="port",default="8000",help="run on the given port",type=int)

if __name__=="__main__":
    app=tornado.web.Application(handlers=[(r"/index",IndexHandler),(r'/get_domain_select',GetDomainHandler),
                                          (r'/get_interfaces_select',GetInterfacesHandler)],
                                template_path=os.path.join(os.path.dirname(__file__),"template"),
                                static_path=os.path.join(os.path.dirname(__file__), "static"))
    httpserver=tornado.httpserver.HTTPServer(app)
    httpserver.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()