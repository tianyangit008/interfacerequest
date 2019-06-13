import pymysql,os
from xml.etree.ElementTree import ElementTree as ET
class Connectdb():
    def connect_db(self,sql):
        try:
            doc=ET().parse(source=os.path.dirname(os.path.dirname(__file__))+'/data/config.xml')
            li=doc.findall('./database/*')
            database_info={}
            for i in li:
               database_info[i.tag]=i.text
            connect=pymysql.Connect(host=database_info.get('host'),port=int(database_info.get('port')),db=database_info.get('db'),user=database_info.get('user')
                                    ,password=database_info.get('password'))
            cursor=connect.cursor()
            cursor.execute(sql)
            connect.commit()
            res=cursor.fetchall()
            return res
        except Exception as e:
            print(e)
        finally:
            connect.close()

if __name__ == '__main__':
   tp=Connectdb().connect_db("select DOMAIN from `performance_statistics` group by DOMAIN")
   print(tp)