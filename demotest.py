res=['xin','fin','aaa']
# str=""
# for i in range(0,len(res)):
#     var=("'%s'," %(res[i]))
#     str +=var
# print(str,end="")
print(",".join(res))

# sql="SELECT INTERFACE FROM `performance_statistics` where DOMAIN IN({args});".format(args=str)
# sql="SELECT INTERFACE FROM `performance_statistics` where DOMAIN IN('A','B');"


