# -*- coding: utf-8 -*-
# @Author       :junjie    
# @Time         :2019/4/9 16:34
# @FileName     :sign_v1_demo.py
#IDE            :PyCharm
#轻瘦，聊吗 时间戳和签名
'''
import time,hashlib,base64
now_time=int(time.time())#获取10位时间戳
m=hashlib.md5()
string=str(now_time)+"L1ght_H!in" #轻瘦key
#string=str(now_time)+"l!a0#ma" 聊吗key
m.update(string.encode('utf-8'))
encodeStr = m.hexdigest()
base_code=base64.b64encode(encodeStr.encode('utf-8'))
print(str(base_code,'utf-8'))
print(now_time)
'''
import time,hashlib,base64
# string='X-MP-SignVer=v1&key=12345678'
# m=hashlib.md5()
# m.update(string.encode("utf8"))
# encodeStr = m.hexdigest()
# base_code=base64.b64encode(encodeStr.encode('utf-8'))

#名品猫sign签名
dict={
    "page": 1,
    "limit":10,
    "name":''
}
my_dict={
    "name":1
}
if not my_dict:
    print("字典为空")
else:
    print("字典不为空")
for key in list(dict.keys()):
    if not dict.get(key):
        del dict[key]
print(dict)
test=sorted(dict.items())
alist=[]
for i in test:
    data='&'+str(i[0])+'='+str(i[1])
    alist.append(data)
list=''.join(alist)
string='X-MP-SignVer=v1'+str(list)+'&key=12345678'
m=hashlib.md5()
m.update(string.encode("utf8"))
encodeStr = m.hexdigest()
base_code=base64.b64encode(encodeStr.encode('utf-8'))
print(str(base_code,'utf-8'))

# for dict_key, dict_value in dict.items():
#     print(dict_key,'=',dict_value)

# print(str(base_code,'utf-8'))