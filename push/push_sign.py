# -*- coding: utf-8 -*-
# @Author       :junjie    
# @Time         :2019/4/19 17:00
# @FileName     :push_sign.py
#IDE            :PyCharm
#封装推送验签
import time,hashlib,base64
from public.config import *
if get('project_type')==0:
    Signkey=get('mpm_key')['sign_key'][get('is_test')]
else:
    Signkey = get('mpwj_key')['sign_key'][get('is_test')]
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
            return self.__sign(string=new_string)
    #私有方法,生成签名
    def __sign(self,string):
        if string:
            sign='X-PUSH-AppVer=1.0.0'+string+'&secret='+Signkey
            m = hashlib.md5()
            m.update(sign.encode("utf8"))
            encodeStr = m.hexdigest()
            base_code = base64.b64encode(encodeStr.encode('utf-8'))
            return str(base_code,'utf-8')
        else:
            sign ='X-PUSH-AppVer=1.0.0' + '&secret='+Signkey
            m = hashlib.md5()
            m.update(sign.encode("utf8"))
            encodeStr = m.hexdigest()
            base_code = base64.b64encode(encodeStr.encode('utf-8'))
            return str(base_code,'utf-8')
    def Utime(self):
        now_time=time.time()
        return int(now_time)
if __name__=='__main__':
    dict={
   "type":"customizedcast",
  "title":"俊杰测试,测试多个alias",
    "ticker":"俊杰测试,测试多个alias",
  "text":"名品猫优惠大促销",
    "subtitle":"苹果测试",
    "body":"苹果通知详情。。。。",
     "productionMode":0,
    "mipush":1,
    "miActivity":1,
    "alias":"67",
    "aliasType":"alias"
}
    Sign=checkSign(dict)
    print(Sign.check_dict())
    print(Sign.Utime())





