# -*- coding: utf-8 -*-
# @Author       :junjie
# @Time         :2020/7/29 10:12
# @FileName     :json2obj.py
# @Motto        :AS the tree,so the fruit
#IDE            :PyCharm

# coding:utf-8
import json


class JSONObject:
    def __init__(self, d):
        """
        类名直接调用 __dict__，会输出该由类中所有类属性组成的字典；而使用类的实例对象调用 __dict__，会输出由类中所有实例属性组成的字典。
        """
        self.__dict__ = d


def json2obj(s):
    # json.loads函数接受参数objec_thook用于指定函数，该函数负责把反序列化后的基本类型对象转换成自定义类型的对象。
    return json.loads(s, object_hook=JSONObject)


def obj2json(a):
    # json.dumps函数接受参数default用于指定一个函数，该函数能够把自定义类型的对象转换成可序列化的基本类型。
    return json.dumps(
        a,
        default=lambda obj: obj.__dict__,
        sort_keys=True,
        indent=4)  # indent=4,这个参数用来更好的展示json


# json.loads 将json字符串转换成python对象dict
# json.dumps 将python对象dict转换成json字符串
a = {
    "data": {
        "cards_tip": "1",
        "service_tip": "0"
    },
    "msg": "success",
    "code": "200"
}
b = json2obj(json.dumps(a))
print(b.msg)

print(obj2json(a))


class JSONObject1:
    def __init__(self, d):
        """
        类名直接调用 __dict__，会输出该由类中所有类属性组成的字典；而使用类的实例对象调用 __dict__，会输出由类中所有实例属性组成的字典。
        """
        self.__dict__ = d


b1 = {"a": 1}
a1 = JSONObject1(b1)
print(a1.__dict__)
