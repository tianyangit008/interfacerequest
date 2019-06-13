from util.connectdb import Connectdb

class Get_select():
    def get_select(self,sql):
        res=Connectdb().connect_db(sql)
        li=[]
        for i in range(0,len(res)):
            data={}
            data["key"]=i
            data["value"]=res[i][0]
            li.insert(i,data)
        return li





