# -*- coding: utf-8 -*-
# @Author       :junjie    
# @Time         :2019/4/24 14:55
# @FileName     :MPM_postman.py
#IDE            :PyCharm
from MPM_Mall.get_requests import getRequests
import json
#目前是APP接口那边的,base_url是mobile
url='user/info/update'
data= {
    "name":"JokerChat"
}
re=getRequests(url,data).get_requests()
print(re)
