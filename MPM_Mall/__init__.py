# -*- coding: utf-8 -*-
# @Author       :junjie    
# @Time         :2019/4/22 20:26
# @FileName     :__init__.py.py
#IDE            :PyCharm
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from public.config import *
from public.common import db_name
db_config=get('db')[db_name[get('project_type')]]
app = Flask(__name__)
app.config['SECRET_KEY']='dev'
app.config['SQLALCHEMY_DATABASE_URI']=db_config
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['JSON_AS_ASCII'] = False
db=SQLAlchemy(app)
from MPM_Mall import views