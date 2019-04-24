# -*- coding: utf-8 -*-
# @Author       :junjie    
# @Time         :2019/3/28 14:32
# @FileName     :dingding_demo.py
#IDE            :PyCharm
from dingtalkchatbot.chatbot import DingtalkChatbot
webhook='https://oapi.dingtalk.com/robot/send?access_token=ab9300b52c6fdb1bd511ce57be6f7e0e3b78ae714ae3ed24795b2c0c67a730d7'
xiaoding=DingtalkChatbot(webhook)
at_mobiles=['+86-18676747031','+86-13265067860','+86-13119656020']
def chengfa():
    for i in range(1,10):
        for j in range(1,i+1):
            print("%d*%d=%2d" % (i,j,i*j),end=" ")
        print (" ")
# Link消息
# xiaoding.send_link(title='这是demo第一版',
#                    text='未完待续...',
#                    message_url='http://www.testclass.net/',
#                    pic_url='https://hxsupload-oss.hxsapp.com/2019-01-28/154866284332491700.jpg?x-oss-process=style/thumb')
dict={
    'name':1,'age':2
}
xiaoding.send_text(msg='',is_at_all=True)