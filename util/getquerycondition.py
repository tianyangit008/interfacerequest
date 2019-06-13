
class GetQueryCondition():

    def get_query_condition(self,params1,params2):
        self.li=[]
        if len(params1) !=0:
            values=params1[0].split(",")
            for i in range(0,len(values)):
                for j in range(0,len(params2)):
                    if(int(values[i]) == params2[j].get("key")):
                        self.li.append(params2[j].get("value"))
        else:
            print("请求参数为空")
        return  self.li

# if __name__=="__main__":
#     li1=['0,1,2']
#     li2=[{"key": 0, "value": "api.fin.youxinjinrong.com"}, {"key": 1, "value": "api.youxinjinrong.com"},
#       {"key": 2, "value": "paysys.youxinjinrong.com"}]
#     var=GetQueryCondition().get_query_condition(li1,li2)
#     print(var)