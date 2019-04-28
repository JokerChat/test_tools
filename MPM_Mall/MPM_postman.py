# -*- coding: utf-8 -*-
# @Author       :junjie    
# @Time         :2019/4/24 14:55
# @FileName     :MPM_postman.py
#IDE            :PyCharm
from MPM_Mall.get_requests import getRequests
import json
#目前是APP接口那边的,base_url是mobile
url='feedback/create'
data= {
    "content": "测试图片上传反馈问题嘻嘻嘻",
    "images":["https://mpmallapp.oss-cn-beijing.aliyuncs.com/feedback/wj5fdebq0rtse2s3dryq.jpg"]
}
re=getRequests(url,data).get_requests()
print(re)
