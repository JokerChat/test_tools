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
    "ticker":"名品猫丨客服",
    "activity":"com.xfhl.umpushlib.MipushTestActivity",
    "productionMode":1,
    "mipush":"1",
    "body":"",
    "title":"名品猫丨客服",
    "type":"customizedcast",
    "platform":"MPM",
    "url":"0",
    "miActivity":"com.xfhl.umpushlib.MipushTestActivity",
    "aliasType":"alias",
    "extra":{
        "link":"http://h5.mingpinmao.cn/help?t=1",
        "type":1
    },
    "subtitle":"尊敬的用户，您购买的商品需要提交身份信息报备入关，由于电讯无法联系到您,请您在获取此通知后及时与我司平台客服取得联系。微信xfhl18024027357",
    "afterOpen":"go_activity",
    "alias":"56",
    "text":"尊敬的用户，您购买的商品需要提交身份信息报备入关，由于电讯无法联系到您,请您在获取此通知后及时与我司平台客服取得联系。微信xfhl18024027357",
    "description":"",
    "production_mode":None,
    "alert":{
        "title":"系统通知",
        "subtitle":"尊敬的用户，您购买的商品需要提交身份信息报备入关，由于电讯无法联系到您,请您在获取此通知后及时与我司平台客服取得联系。微信xfhl18024027357",
        "body":"名品猫丨客服"
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
