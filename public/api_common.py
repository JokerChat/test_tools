# -*- coding: utf-8 -*-
# @Author       :junjie    
# @Time         :2020/5/29 15:13
# @FileName     :api_common.py
# @Motto        :AS the tree,so the fruit
#IDE            :PyCharm
from public.config import get


base_url=['mpm_url','xfyl_url','zhuanbo_url','lexuan_url']

sign=['mpm','xfyl','zhuanbo','lexuan']

db_name=['db_mpm','db_xfyl','db_zhuanbo','db_lexuan']

params=['mpm_params','xfyl_params','zb_params','lexuan_params']

public_header =['mpm_public_header','xfyl_public_header','zb_public_header','lexuan_public_header']

aes_project=['xfyl_aes','lexuan_aes']

api_url=get(base_url[get('api_project_type')])[get('api_is_test')] #接口url

api_sign=get(sign[get('api_project_type')])[get('api_is_test')] #鉴权key

api_params=get(params[get('api_project_type')]) #公共参数

api_header=get(public_header[get('api_project_type')]) #请求头

api_db=get(db_name[get('api_project_type')]) # 数据库设置

dingding_token=get('dingding_token') #钉钉token

dingding_secret=get('dingding_secret') #钉钉验签key

project_type = get('api_project_type') # 项目类型

if project_type==1:
    api_aes_key=get('xfyl_aes')['key'][get('api_is_test')]
    api_aes_iv=get('xfyl_aes')['iv'][get('api_is_test')]
elif project_type==3:
    api_aes_key = get('lexuan_aes')['key'][get('api_is_test')]
    api_aes_iv = get('lexuan_aes')['iv'][get('api_is_test')]

pass
