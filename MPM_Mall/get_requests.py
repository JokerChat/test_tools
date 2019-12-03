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
from public.common import url
mylog=logger('接口测试').get_logger()
base_url =get(url[get('project_type')])[get('is_test')]
class getRequests:
    def __init__(self,url,data):
        self.url=base_url+url
        self.data=data
    def get_requests(self):
        try:
            r = requests.post(self.url,headers=self.__header(self.data),data=json.dumps(self.data))
            mylog.info("########请求头信息：{}########".format(json.dumps(self.__header(self.data))))
            mylog.info("########请求参数：{}########".format(json.dumps(self.data), ensure_ascii=False))
            mylog.info("########返回数据：{}########".format(json.dumps(r.json(), ensure_ascii=False)))
            '''
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
            '''
            return r.json()
        except Exception as e:
            print(e)
            '''
            mylog.info("############请求失败,原因:{}############".format(e))
            erro_msg="服务器响应异常，HTTP状态码：{0}，响应内容：{1}".format(r.status_code, r.text)
            self.__dingding(str(erro_msg))
            mylog.info("服务器响应异常，状态码：%s，响应内容：%s" % (r.status_code, r.text))
            '''
    #请求头
    def __header(self,data):
        header = {
            'Content-Type': 'application/json',
            'X-MPMALL-Signver':'v1',
            'X-MPMALL-Token': get('token')
        }
        sign = checkSign(data).check_dict()
        header['X-MPMALL-Sign']=sign
        return header
    #钉钉发消息
    def __dingding(self,msg):
        webhook = 'https://oapi.dingtalk.com/robot/send?access_token='+get('dingding_token')
        xiaoding = DingtalkChatbot(webhook)
        xiaoding.send_text(msg=msg, is_at_all=False)
if __name__=='__main__':
    url='auth/login'
    data= {
		"code": "0",
		"mobile": str(mobile),
		"inviteCode": inviteCode,
		"mercId": "888000000000003",
		"platform": "XFYLMALL",
		"sysCnl": "H5",
		"timestamp": "1574066264"
	}
    re=getRequests(url,data).get_requests()