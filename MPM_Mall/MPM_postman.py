# -*- coding: utf-8 -*-
# @Author       :junjie
# @Time         :2019/4/24 14:55
# @FileName     :MPM_postman.py
#IDE            :PyCharm
from MPM_Mall.handle_requests import HandleRequests
# 目前是APP接口那边的,base_url是mobile
url='auth/login'
data= {
	"mobile": "13119656020",
	"password": "123",
	"type": "2",
}
do_request=HandleRequests()
res = do_request.send("POST", url, json=data)
print(res.json())