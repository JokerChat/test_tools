# -*- coding: utf-8 -*-
# @Author       :junjie    
# @Time         :2019/5/15 11:58
# @FileName     :re_demo.py
#IDE            :PyCharm
#实现在多维嵌套字典、列表、元组的JSON中获取数据，兼容多个相同的key
def get_target_value(key, dic, tmp_list):
    """
    :param key: 目标key值
    :param dic: JSON数据
    :param tmp_list: 用于存储获取的数据
    :return: list
    """
    if not isinstance(dic, dict) or not isinstance(tmp_list, list):  # 对传入数据进行格式校验
        return '传入数据格式有误'

    if key in dic.keys():
        tmp_list.append(dic[key])  #目标值存在则存入tmp_list
    else:
        for value in dic.values():  # 目标值不存在，则对其value值进行遍历
            if isinstance(value, dict): #判断value是否为字典
                get_target_value(key, value, tmp_list)  # 传入数据的value值是字典，则直接调用自身
            elif isinstance(value, (list, tuple)): #判断value是否为列表或者元祖
                __get_value(key, value, tmp_list)  # 传入数据的value值是列表或者元组，则调用_get_value
    return tmp_list
def __get_value(key, val, tmp_list):
    for val_ in val:
        if isinstance(val_, dict):
            get_target_value(key, val_, tmp_list)  # 传入数据的value值是字典，则调用get_target_value
        elif isinstance(val_, (list, tuple)):
            __get_value(key, val_, tmp_list)   # 传入数据的value值是列表或者元组，则调用自身
if __name__=='__main__':

    data = {'msg': '成功', 'code': 10000, 'data': {'total': '13',
                                                 'comment': {'id': 672, 'pid': 0, 'dynamicId': 35, 'fromUid': 67,
                                                             'content': '测试评论', 'fromUserName': '我是大美人',
                                                             'headImgUrl': 'https://img.xiaohongshu.com/avatar/5c2c36af2090e000012ed003.jpg@240w_240h_90q_1e_1c_1x.jpg',
                                                             'toUserName': '', 'dynamicTime': '刚刚',
                                                             'addTime': '2019-05-15 16:58:42', 'isOwn': True}}}

    '''
    data ={'msg':'成功','code':200,'data':[{
			"id": "001ec588eb8b467cb16c50552bf1e696",
			"code": "LS003",
			"name": "水光丝绒修颜乳",
			"productUnitName": "瓶",
			"productUnitId": 0,
			"productTypeName": "隔离",
			"specificationsCount": 30,
			"specificationsUnitName": "毫升",
			"stockCount": 0,
			"safeCount": 0,
			"salePrice": "235",
			"productOrigin": "纤体",
			"isOnline": 0,
			"isSync": 1,
			"isOnlineStr": 'null',
			"remark": ""
		}, {
			"id": "006fa1d8617d4b71a075bafb82e3a0d1",
			"code": "LS020",
			"name": "净颜修护精华液",
			"productUnitName": "瓶",
			"productUnitId": 0,
			"productTypeName": "修复",
			"specificationsCount": 15,
			"specificationsUnitName": "毫升",
			"stockCount": 0,
			"safeCount": 0,
			"salePrice": "220",
			"productOrigin": "纤体",
			"isOnline": 0,
			"isSync": 1,
			"isOnlineStr": 'null',
			"remark": ""
		}]}
		'''
    id=get_target_value('id',data,[])
    print(id)