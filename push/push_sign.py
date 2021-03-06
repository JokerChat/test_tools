# -*- coding: utf-8 -*-
# @Author       :junjie    
# @Time         :2019/4/19 17:00
# @FileName     :push_sign.py
#IDE            :PyCharm
#封装推送验签
import time,hashlib,base64
from public.push_common import push_sign_key,push_header_key
class checkSign:
    #初始化传入dict
    def __init__(self,dict):
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
            return {'Content-Type':'application/json',
                    'X-PUSH-AppVer': '1.0.0',
                    'X-PUSH-AppKey':push_header_key,
                    'X-PUSH-Sign':self.__sign(string=new_string),
                    'X-PUSH-Utime':str(int(time.time()))}
    #私有方法,生成签名
    def __sign(self,string):
        if string:
            sign='X-PUSH-AppVer=1.0.0'+string+'&secret='+push_sign_key
            m = hashlib.md5()
            m.update(sign.encode("utf8"))
            encodeStr = m.hexdigest()
            base_code = base64.b64encode(encodeStr.encode('utf-8'))
            return str(base_code,'utf-8')
        else:
            sign ='X-PUSH-AppVer=1.0.0' + '&secret='+push_sign_key
            m = hashlib.md5()
            m.update(sign.encode("utf8"))
            encodeStr = m.hexdigest()
            base_code = base64.b64encode(encodeStr.encode('utf-8'))
            return str(base_code,'utf-8')


if __name__=='__main__':
    dict={
   "a":123,
    "b":"b ss"
}
    Sign=checkSign(dict)
    print(Sign.check_dict())





