# -*- coding: utf-8 -*-
# @Author       :junjie    
# @Time         :2019/4/24 14:55
# @FileName     :MPM_postman.py
#IDE            :PyCharm
from MPM_Mall.get_requests import getRequests
import json
#目前是APP接口那边的,base_url是mobile
url='ad/list'
data= {
            "position":3
}
re=getRequests(url,data).get_requests()
json_dict=json.dumps(re,sort_keys=True,indent=4,ensure_ascii=False)
print(json_dict)
