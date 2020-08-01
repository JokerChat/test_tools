# -*- coding: utf-8 -*-
# @Author       :junjie    
# @Time         :2020/5/25 15:41
# @FileName     :config_path.py
# @Motto        :AS the tree,so the fruit
#IDE            :PyCharm

import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CONF_PATH = os.path.join(BASE_DIR, "confs") #配置文件根路径

CONF_FILE_PATH = os.path.join(CONF_PATH, "config.yaml") #配置文件路径

PUBLIC_FILE_PATH = os.path.join(CONF_PATH, "public_key_pkcs8.pem") #公钥路径

PRIVATE_FILE_PATH = os.path.join(CONF_PATH, "private_key_pkcs1.pem") #私钥路径

pass

