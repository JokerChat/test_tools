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
data={
    "ticker":"恭喜你升级为M司令（高级合伙人）",
    "activity":"com.xfhl.umpushlib.MipushTestActivity",
    "productionMode":1,
    "mipush":"1",
    "body":"",
    "title":"系统通知",
    "type":"customizedcast",
    "platform":"MPWJMALL",
    "url":"0",
    "miActivity":"com.xfhl.umpushlib.MipushTestActivity",
    "aliasType":"alias",
    "extra":{
        "link":"",
        "type":3
    },
    "subtitle":"恭喜你升级为M司令（高级合伙人）",
    "afterOpen":"go_activity",
    "alias":"703",
    "startTime":"2019-09-05 16:39:26",
    "text":"恭喜你升级为M司令（高级合伙z人）",
    "description":"",
    "production_mode":None,
    "start_time":"2019-09-05 16:39:26",
    "alert":{
        "title":"系统通知",
        "subtitle":"恭喜你升级为M司令（高级合伙人）",
        "body":""
    }
}

# data= {
#    "taskId":"fe1e1655ea25b5645b0b484beb32cb9d"
# }

# re=getRequests(url,data).get_requests()



index=0
while 1:
    re=getRequests(url,data).get_requests()
    index +=1
    print("推送成功")
    time.sleep(5)
    if index ==60:
        break
