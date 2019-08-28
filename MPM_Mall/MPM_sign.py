# -*- coding: utf-8 -*-
# @Author       :junjie    
# @Time         :2019/4/22 20:37
# @FileName     :MPM_sign.py
#IDE            :PyCharm
import hashlib,base64
from public.config import *
if get('is_test')==0:
    Signkey=get('sign_key')[0]
else:
    Signkey = get('sign_key')[1]
class checkSign:
    #初始化传入dict
    def __init__(self,dict):
        #不改变传入的data=>直接对字典进行复制
        data=dict.copy()
        self.dict=data
    def check_dict(self):
        #首先判断字典是否空,为空直接加密
        if not self.dict:
            string =''
            return self.__sign(string=string)
        else:
        # 非空字典,过滤value为空和嵌套字典、列表
            for k,v in list(self.dict.items()):
                if v=='' or v==None:
                    self.dict.pop(k)
                for k, v in list(self.dict.items()):
                    if type(self.dict[k]).__name__=='dict'or type(self.dict[k]).__name__=='list':
                        self.dict.pop(k)
            #对字典进行ASCII码排序
            new_list = sorted(self.dict.items())
            alist = []
            for i in new_list:
                data = '&'+str(i[0]) + '=' + str(i[1])
                alist.append(data)
            new_string = ''.join(alist)
            return self.__sign(string=new_string)
    #私有方法,生成签名
    def __sign(self,string):
        if string:
            sign=string[1:]+'&key='+Signkey#测试环境
            m = hashlib.md5()
            m.update(sign.encode("utf8"))
            encodeStr = m.hexdigest()
            base_code = base64.b64encode(encodeStr.encode('utf-8'))
            return str(base_code,'utf-8')
        else:
            sign ='key='+Signkey
            m = hashlib.md5()
            m.update(sign.encode("utf8"))
            encodeStr = m.hexdigest()
            base_code = base64.b64encode(encodeStr.encode('utf-8'))
            return str(base_code,'utf-8')
if __name__=='__main__':
    dict={}
    Sign = checkSign(dict)
    print(Sign.check_dict())
    print(dict)
