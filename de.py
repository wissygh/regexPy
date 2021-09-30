import os
import numpy as np
import re
with open("replace.txt") as txt:
  contents = txt.readlines() #读全部行
  txt.close()
# lines =np.array(content) #转换成array 类型
# num_of_instances = lines.size #整个txt的行数
# print("number of instances: ", num_of_instances)
# list=[]
F = open("re_new.txt", 'w')

def addval(matched):
    if(matched):
        value = matched.group('value')
        return ("|  io.insnRdata(31,20) === " + value)
    else:
        return 0

for content in contents:
    content = str(content)
    content = re.sub("(?P<value>(CSR_))", addval, content)
    F.writelines(content)#写入到另一个txt文件中
F.close()
