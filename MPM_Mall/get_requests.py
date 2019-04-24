# -*- coding: utf-8 -*-
# @Author       :junjie    
# @Time         :2019/4/22 20:27
# @FileName     :get_requests.py
#IDE            :PyCharm
import requests,json
from public.log import logger
from MPM_Mall.MPM_sign import checkSign
from dingtalkchatbot.chatbot import DingtalkChatbot
mylog=logger('名品猫接口测试').get_logger()
base_url='http://api-test.mingpinmao.cn/shop/mobile/'
class getRequests:
    def __init__(self,url,data):
        self.url=base_url+url
        self.data=data
    def get_requests(self):
        try:
            r = requests.post(self.url,headers=self.__header(self.data),data=json.dumps(self.data))
            if r.json()['code']!=10000:
                erro_msg='接口请求错误,返回code值是'+str(r.json()['code'])+'\n'+'json数据：'+'\n'+str(r.json())
                self.__dingding(str(erro_msg))
                mylog.info("########请求数据：{}########".format(json.dumps(self.data)))
            else:
                mylog.info("########请求头信息：{}########".format(self.__header(self.data)))
                mylog.info("########请求参数：{}########".format(self.data))
                mylog.info("########返回数据：{}########".format(r.json()))
                msg='返回数据是：'+'\n'+str(r.json())+'\n'
                self.__dingding(str(msg))
                return r.json()
        except Exception as e:
            mylog.info("############请求失败,原因:{}############".format(e))
            erro_msg="服务器响应异常，HTTP状态码：{0}，响应内容：{1}".format(r.status_code, r.text)
            self.__dingding(str(erro_msg))
            mylog.info("服务器响应异常，状态码：%s，响应内容：%s" % (r.status_code, r.text))
    #请求头
    def __header(self,data):
        header = {
            'Content-Type': 'application/json',
            'X-MP-SignVer':'v1'
        }
        sign = checkSign(data).check_dict()
        header['X-MP-Sign']=sign
        return header
    #钉钉发消息
    def __dingding(self,msg):
        webhook = 'https://oapi.dingtalk.com/robot/send?access_token=ab9300b52c6fdb1bd511ce57be6f7e0e3b78ae714ae3ed24795b2c0c67a730d7'
        xiaoding = DingtalkChatbot(webhook)
        xiaoding.send_text(msg=msg, is_at_all=False)
if __name__=='__main__':
    url='ad/list'
    data= {
            "position":1
}
    re=getRequests(url,data).get_requests()