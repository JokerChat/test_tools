# -*- coding: utf-8 -*-
# @Author       :junjie    
# @Time         :2019/4/22 10:12
# @FileName     :push_postman.py
#IDE            :PyCharm
from push.push_requests import getRequests
import time
import datetime
url='send'
now_time=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
data= {
   "type":"customizedcast",
  "title":"收到了吗？"+now_time,
    "ticker":"test"+now_time,
  "text":"收到了吗？"+now_time,
    "subtitle":"test"+now_time,
    "body":"收到了吗？"+now_time,
     "productionMode":0,
    "alias": 67,
    "extra":{"A":123,"B":123344},
    "aliasType":"alias",
}
# data= {
#    "taskId":"fe1e1655ea25b5645b0b484beb32cb9d"
# }
index=0
while 1:
    re=getRequests(url,data).get_requests()
    index +=1
    print("推送成功")
    time.sleep(5)
    if index ==60:
        break
