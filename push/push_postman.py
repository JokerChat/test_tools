# -*- coding: utf-8 -*-
# @Author       :junjie    
# @Time         :2019/4/22 10:12
# @FileName     :push_postman.py
#IDE            :PyCharm
from push.push_requests import getRequests
url='send'
data= {
   "type":"broadcast",
  "title":"测试模式",
    "ticker":"test 2019年5月30日16:33:03",
  "text":"名品猫优惠大促销",
    "subtitle":"test",
    "body":"苹果通知详情。。。。",
     "productionMode":0,
}
# data= {
#    "taskId":"fe1e1655ea25b5645b0b484beb32cb9d"
# }
re=getRequests(url,data).get_requests()
print(re)