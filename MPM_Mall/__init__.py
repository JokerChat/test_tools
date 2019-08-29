# -*- coding: utf-8 -*-
# @Author       :junjie    
# @Time         :2019/4/22 20:26
# @FileName     :__init__.py.py
#IDE            :PyCharm
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from public.config import *
db_config=get('db')['mpm']
app = Flask(__name__)
app.config['SECRET_KEY']='dev'
app.config['SQLALCHEMY_DATABASE_URI']=db_config
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)
from MPM_Mall import views