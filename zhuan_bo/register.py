# -*- coding: utf-8 -*-
# @Author       :junjie    
# @Time         :2019/11/18 16:34
# @FileName     :register.py
#IDE            :PyCharm
from MPM_Mall.get_requests import getRequests
# 目前是APP接口那边的,base_url是mobile
url1='auth/code'
url2='auth/login/mp'
mobile=13717276540
index=0
inviteCode=157434
while True:
	data1={
	"type": 1,
	"areaCode": "86",
	"mobile": str(mobile),
	"mercId": "888000000000004",
	"platform": "ZBMALL",
	"sysCnl": "H5",
	"timestamp": "1574066250"
	}
	if index==10:
		break
	getRequests(url1, data1).get_requests()
	data2 = {
		"code": "0",
		"mobile": str(mobile),
		"inviteCode": inviteCode,
		"mercId": "888000000000004",
		"platform": "ZBMALL",
		"sysCnl": "H5",
		"timestamp": "1574066264"
	}
	new_inviteCode=getRequests(url2, data2).get_requests()['data']['inviteCode']
	inviteCode=new_inviteCode
	mobile+=1
	index+=1

