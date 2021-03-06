# -*- coding: utf-8 -*-
#封装request方法
import requests,json
from public.log import logger
from push.push_sign import checkSign
from dingtalkchatbot.chatbot import DingtalkChatbot
from public.push_common import push_url,dingding_token,dingding_secret

mylog=logger('push接口测试').get_logger()

class getRequests:
    def __init__(self,url,data):
        self.url = push_url+url
        self.data=data
    def get_requests(self):
        try:
            r = requests.post(self.url,headers=self.__header(self.data),data=json.dumps(self.data))
            msg = json.dumps(r.json(), ensure_ascii=False)
            if r.status_code==200:
                if int(r.json()['code']) ==0:
                    ding_msg='接口测试成功'+'\n'+'返回数据是：'+'\n'+str(msg)
                    self.__dingding(ding_msg)
                else:
                    requests_data=json.dumps(self.data,ensure_ascii=False)
                    ding_msg = '接口测试失败,不符合业务code' +'\n'+ '请求参数是：'+'\n'+str(requests_data)+'\n'+'返回数据是：'+'\n'+str(msg)
                    self.__dingding(ding_msg)
            else:
                mylog.info("########接口请求失败：{}########".format(r.status_code))
                self.__dingding(str(msg))
            mylog.info("########请求数据：{}########".format(json.dumps(self.data)))
            mylog.info("########返回数据：{}########".format(json.dumps(r.json())))
            return r.json()
        except Exception as e:
            mylog.info("############请求失败,原因:{}############".format(e))
            erro_msg="服务器响应异常，状态码：{0}，响应内容：{1}".format(r.status_code, r.text)
            self.__dingding(str(erro_msg))
            mylog.info("服务器响应异常，状态码：%s，响应内容：%s" % (r.status_code, r.text))
    def __header(self,data):

        header_data = checkSign(data).check_dict()

        return header_data

    #钉钉发消息
    def __dingding(self,msg):
        webhook = 'https://oapi.dingtalk.com/robot/send?access_token=' + dingding_token
        xiaoding = DingtalkChatbot(webhook, dingding_secret)
        xiaoding.send_text(msg, is_at_all=False)
if __name__=='__main__':
    url='send'
    data= {
   "type":"broadcast",
  "title":"测试通知标题最好40个字符串",
    "ticker":"这是安卓的通知栏提示文字",
  "text":"这是安卓的通知文字描述",
    "subtitle":"苹果测试",
    "body":"苹果通知详情。。。。",
     "productionMode":0
}
    re=getRequests(url,data).get_requests()
    print(re)