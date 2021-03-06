# -*- coding: utf-8 -*-
# @Author       :junjie    
# @Time         :2019/4/22 20:26
# @FileName     :__init__.py.py
#IDE            :PyCharm
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from public.api_common import api_db
app = Flask(__name__)
app.config['SECRET_KEY']='dev'
app.config['SQLALCHEMY_DATABASE_URI']=api_db
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True     #    每次请求结束后都会自动提交数据库中的变动
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['JSON_AS_ASCII'] = False
db=SQLAlchemy(app)
from MPM_Mall import views,lexuan_views