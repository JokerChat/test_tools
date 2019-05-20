# -*- coding: utf-8 -*-
# @Author       :junjie    
# @Time         :2019/4/22 10:12
# @FileName     :push.py
#IDE            :PyCharm
from demo.test_requests import getRequests
url='send'
# data= {
#    "type":"broadcast",
#   "title":"正式模式",
#     "ticker":"正式模式2019年5月6日21:44:57",
#   "text":"名品猫优惠大促销",
#     "subtitle":"正式模式2019年5月6日21:45:15",
#     "body":"苹果通知详情。。。。",
#      "productionMode":1,
# }
data= {
   "type":"customizedcast",
  "title":"这是正式模式",
    "ticker":"这是正式安卓",
  "text":"名品猫优惠大促销",
    "subtitle":"这是测试模式2019年5月9日11:14:42",
    "body":"苹果通知详情。。。。",
    "alias":67,
    "aliasType":"alias",
     "productionMode":1,
}
re=getRequests(url,data).get_requests()