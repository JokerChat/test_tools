# -*- coding: utf-8 -*-
# @Author       :junjie    
# @Time         :2019/4/22 20:27
# @FileName     :handle_requests.py
#IDE            :PyCharm
import requests,json
from public.log import logger
from MPM_Mall.MPM_sign import checkSign
from dingtalkchatbot.chatbot import DingtalkChatbot
from public.config import get
from public.api_common import api_params,api_url,api_header,dingding_token,dingding_secret
import time



class HandleRequests:
    def __init__(self):
        #获取公共请求参数
        self.public_params=api_params
        #获取请求url
        self.url=api_url
        #创建会话对象
        self.session=requests.Session()
        #将公共请求头放在会话对象中
        self.add_header(api_header)


    def add_header(self,header_dict):
        """

        :param header_dict:添加请求头,字典格式
        :return: None
        """
        self.session.headers.update(header_dict)

    def send(self,method,url,**kwargs):
        """

        :param method:请求方式
        :param url: 请求url
        :param kwargs:header 请求头,data、json、files
        :return:返回请求对象
        """

        kwargs["json"] = self.handle_param("json", kwargs)
        kwargs["data"] = self.handle_param("data", kwargs)
        if kwargs["json"] is not None:
            timestamp = int(time.time())
            self.public_params.update({"timestamp": timestamp})
            kwargs["json"].update(self.public_params)
            sign=checkSign(kwargs["json"]).check_dict()
            self.add_header(sign)
        elif kwargs["data"] is not None:
            timestamp = int(time.time())
            self.public_params.update({"timestamp": timestamp})
            kwargs["data"].update(self.public_params)
            sign = checkSign(kwargs["data"]).check_dict()
            self.add_header(sign)
        new_url=self.url+url
        return self.session.request(method.upper(),new_url,**kwargs)


    @staticmethod
    def handle_param(param_name,param_dict):
        """

        :param param_name:传json或者data
        :param param_dict: 字典格式
        :return:
        """
        if param_name in param_dict:
            data=param_dict.get(param_name)
            if isinstance(data,str):
                try:
                    data=json.loads(data)
                except Exception:
                    data=eval(data)
            return data

    def head(self):
        return self.session.headers

    @staticmethod
    #钉钉发消息
    def dingding(msg):
        webhook = 'https://oapi.dingtalk.com/robot/send?access_token='+dingding_token
        xiaoding = DingtalkChatbot(webhook,dingding_secret)
        xiaoding.send_text(msg, is_at_all=False)
if __name__=='__main__':
    url='base/send/sms'
    data={
	"smsType": 2,
	"mobile": "13119651111",
}
    do_request=HandleRequests()
    res = do_request.send("POST", url,json=data)
    print(res.json())
    # HandleRequests.dingding(res.text)
