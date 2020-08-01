# -*- coding: utf-8 -*-
# @Author       :junjie    
# @Time         :2019/8/28 10:01
# @FileName     :config.py
#IDE            :PyCharm
import os
import copy as mycopy
import yaml

from public.config_path import CONF_FILE_PATH
__all__ = ['set', 'get', 'copy', 'update', '_print']

def get_yaml():
    """
    解析 yaml
    :return: s  字典
    """
    try:

        with open(CONF_FILE_PATH, 'r', encoding='utf-8') as file:
            config = yaml.safe_load(file)
            # config = yaml.load(file, Loader=yaml.Loader)
        return config
    except Exception as exception:
        print(str(exception))
        print('你的config.yaml 文件配置出错...')
    return None


opts = get_yaml()
def set(key, value):
    """ 通过 key 设置某一项值 """
    opts[key] = value


def get(key, default=None):
    """ 通过 key 获取值 """
    return opts.get(key, default)


def copy():
    """ 复制配置 """
    return mycopy.deepcopy(opts)


def update(new_opts):
    """ 全部替换配置 """
    opts.update(new_opts)


def _print():
    print(opts)


if __name__ == '__main__':
    _print()