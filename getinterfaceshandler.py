import tornado.web
import json
from util.connectdb import Connectdb
from util.getselect import Get_select
from getdomainhandler import GetDomainHandler
from util.getquerycondition import GetQueryCondition

class  GetInterfacesHandler(tornado.web.RequestHandler):

    def select_interfaces(self,arg1):
        domain_li = GetDomainHandler.select_domain()
        res=GetQueryCondition().get_query_condition(arg1, domain_li)
        # res是一个list,每个元素为域名

    def get(self):
        domain=self.get_arguments("domain")

