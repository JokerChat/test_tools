# -*- coding: utf-8 -*-
# @Author       :junjie    
# @Time         :2019/9/10 14:24
# @FileName     :push_common.py
#IDE            :PyCharm\

from public.config import get

push_project_type=['mpm_key','mpwj_key','mwj_key','xfyl_key','mzwj_key']

push_header_key=get(push_project_type[get('push_project_type')])['header_key'][get('push_is_test')] #推送请求头key

push_sign_key=get(push_project_type[get('push_project_type')])['sign_key'][get('push_is_test')] #推送sign鉴权key

push_url=get('push_url')[get('push_is_test')] #推送url

dingding_token=get('dingding_token') #钉钉token

dingding_secret=get('dingding_secret') #钉钉验签key

pass


