# -*- coding: utf-8 -*-
# @Author       :junjie    
# @Time         :2019/12/4 14:57
# @FileName     :findFile.py
#IDE            :PyCharm


#遍历目录，输出目录存在文件个数
import os
def filenum(path):
    if os.path.isfile(path):
        print(path)
        print('file num is 1 ')
        return
    num=0
    file_num=0
    for i in (os.listdir(path)):
        filepath=os.path.join(path,i)
        if os.path.isfile(filepath):
            num+=1
            print('文件是：%s'%filepath)
        else:
            print('当前目录%s'%filepath)
            file_num+=1
            filenum(filepath)
    print('当前文件数量:%s'%num,'当前文件夹数量%s'%file_num,
    '路径是:%s'%(path))
filenum('C:/Users/junjie/Desktop/jmeter/com/lvshou/testing')