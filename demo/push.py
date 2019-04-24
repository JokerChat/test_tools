# -*- coding: utf-8 -*-
# @Author       :junjie    
# @Time         :2019/4/22 10:12
# @FileName     :push.py
#IDE            :PyCharm
from demo.test_requests import getRequests
url='send'
data= {
   "type":"customizedcast",
  "title":"俊杰测试,测试多个alias",
    "ticker":"俊杰测试,测试多个alias",
  "text":"名品猫优惠大促销",
    "subtitle":"苹果测试",
    "body":"苹果通知详情。。。。",
     "productionMode":0,
    "mipush":1,
    "miActivity":1,
    "alias":"67",
    "aliasType":"alias"
}
re=getRequests(url,data).get_requests()