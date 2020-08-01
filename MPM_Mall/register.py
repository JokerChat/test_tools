# -*- coding: utf-8 -*-
# @Author       :junjie
# @Time         :2019/11/18 16:34
# @FileName     :register.py
#IDE            :PyCharm
from MPM_Mall.handle_requests import HandleRequests


# 批量注册，直属关系。
def batch_register(mobile, inviteCode, total):
    url1 = 'base/send/sms'
    url2 = 'user/moblie/register'
    index = 0
    do_request = HandleRequests()
    while True:
        data1 = {
            "smsType": 2,
            "mobile": str(mobile),
            "isAct": 1
        }
        data2 = {
            "password": "123",
            "mobile": str(mobile),
            "smsType": 2,
            "smsCode": "0",
            "inviteCode": inviteCode
        }
        if index == total:
            break
        res1 = do_request.send("POST", url1, json=data1)
        print(res1.json())
        res2 = do_request.send("POST", url2, json=data2)
        print(res2.json())
        mobile += 1
        index += 1

# 批量注册，邀请链条


def recursion_register(mobile, inviteCode, total):
    url1 = 'base/send/sms'
    url2 = 'user/moblie/register'
    index = 0
    do_request = HandleRequests()
    while True:
        data1 = {
            "smsType": 2,
            "mobile": str(mobile),
            "isAct": 1
        }
        data2 = {
            "password": "123",
            "mobile": str(mobile),
            "smsType": 2,
            "smsCode": "0",
            "inviteCode": inviteCode
        }
        if index == total:
            break
        res1 = do_request.send("POST", url1, json=data1)
        print(res1.json())
        res2 = do_request.send("POST", url2, json=data2)
        print(res2.json())
        inviteCode = res2.json()['data']['inviteCode']
        mobile += 1
        index += 1


if __name__ == '__main__':
    batch_register(13119656040, 'Y5260802', 10)
