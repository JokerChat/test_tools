# -*- coding: utf-8 -*-
# @Author       :junjie    
# @Time         :2019/11/18 16:34
# @FileName     :register.py
#IDE            :PyCharm
from MPM_Mall.get_requests import getRequests
# 目前是APP接口那边的,base_url是mobile
url1='auth/code'
url2='auth/login/mp'
mobile=13717176513
index=0
inviteCode=140485
while True:
	data1={
	"type": 1,
	"areaCode": "86",
	"mobile": str(mobile),
	"mercId": "888000000000003",
	"platform": "XFYLMALL",
	"sysCnl": "H5",
	"timestamp": "1574066250"
	}
	data2={
		"code": "0",
		"mobile": str(mobile),
		"inviteCode": inviteCode,
		"mercId": "888000000000003",
		"platform": "XFYLMALL",
		"sysCnl": "H5",
		"timestamp": "1574066264"
	}
	if index==1:
		break
	getRequests(url1, data1).get_requests()
	getRequests(url2, data2).get_requests()
	mobile+=1
	index+=1

