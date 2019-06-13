import tornado.web
import json
from util.connectdb import Connectdb
from util.getselect import Get_select

class  GetDomainHandler(tornado.web.RequestHandler):
    @classmethod
    def get_domain(cls,sql):
        return Get_select().get_select(sql)
    @classmethod
    def select_domain(cls):
        # 获取实际查询域名数据
        sql = "select DOMAIN from performance_statistics group by DOMAIN"
        return cls.get_domain(sql)

    def get(self):
        # 发送域名数据
        domain_data=self.select_domain()
        self.write(json.dumps(domain_data))
