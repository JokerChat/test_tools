# -*- coding: utf-8 -*-
# @Author       :junjie    
# @Time         :2019/6/5 17:29
# @FileName     :run.py
#IDE            :PyCharm
from MPM_Mall import app
app.run(
    host='0.0.0.0',
    port=4000,
    debug=True
)