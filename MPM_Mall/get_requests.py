# -*- coding: utf-8 -*-
# @Author       :junjie    
# @Time         :2019/4/22 20:27
# @FileName     :get_requests.py
#IDE            :PyCharm
import requests,json
from public.log import logger
from MPM_Mall.MPM_sign import checkSign
from dingtalkchatbot.chatbot import DingtalkChatbot
from public.config import *
mylog=logger('名品猫接口测试').get_logger()
if get('is_test')==0:
    base_url=get('APP_url').get('test-url')
else:
    base_url = get('APP_url').get('pro-url')
class getRequests:
    def __init__(self,url,data):
        self.url=base_url+url
        self.data=data
    def get_requests(self):
        try:
            r = requests.post(self.url,headers=self.__header(self.data),data=json.dumps(self.data))
            msg = json.dumps(r.json(), ensure_ascii=False)
            mylog.info("########请求头信息：{}########".format(json.dumps(self.__header(self.data))))
            mylog.info("########请求参数：{}########".format(json.dumps(self.data), ensure_ascii=False))
            mylog.info("########返回数据：{}########".format(json.dumps(r.json(), ensure_ascii=False)))
            if r.json()['code']!=10000:
                requests_data = json.dumps(self.data, ensure_ascii=False)
                ding_msg = '接口测试失败,不符合业务code' +'\n'+ '请求参数是：' + '\n' + str(requests_data) + '\n' + '返回数据是：' + '\n' + str( msg)
                self.__dingding(ding_msg)
            else:
                ding_msg = '接口测试成功' + '\n' + '返回数据是：' + '\n' + str(msg)
                self.__dingding(ding_msg)
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
            'X-MP-SignVer':'v1',
            'X-MPMall-Token':'s8aqs53v5aof1fp063xvfa8lhn6lmds2'
        }
        sign = checkSign(data).check_dict()
        header['X-MP-Sign']=sign
        return header
    #钉钉发消息
    def __dingding(self,msg):
        webhook = 'https://oapi.dingtalk.com/robot/send?access_token='+get('dingding_token')
        xiaoding = DingtalkChatbot(webhook)
        xiaoding.send_text(msg=msg, is_at_all=False)
if __name__=='__main__':
    url='auth/login'
    data= {
            "mobile":"13119656020",
            "password":"123",
            "type":2
}
    re=getRequests(url,data).get_requests()