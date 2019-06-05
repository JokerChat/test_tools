# -*- coding: utf-8 -*-
# @Author       :junjie    
# @Time         :2019/3/29 8:48
# @FileName     :random_json_demo.py
#IDE            :PyCharm
import random
data={
	"status": 200,
	"message": "OK",
	"data": {
		"page": 1,
		"size": 10,
		"data": [{
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
		}, {
			"id": "01b2380e88fc45a886111a6d8f880243",
			"code": "K030",
			"name": "悦颜多元焕能防护乳",
			"productUnitName": "瓶",
			"productUnitId": 0,
			"productTypeName": "补水",
			"specificationsCount": 35,
			"specificationsUnitName": "克",
			"stockCount": 0,
			"safeCount": 0,
			"salePrice": "498",
			"productOrigin": "纤体",
			"isOnline": 0,
			"isSync": 1,
			"isOnlineStr": 'null',
			"remark": ""
		}, {
			"id": "0ea23cd023144fae8dfe88282bcb12f2",
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
		}, {
			"id": "100e15f229fa469cbc85086aced9bfda",
			"code": "K033",
			"name": "金钻眼部水漾精萃凝露",
			"productUnitName": "瓶",
			"productUnitId": 0,
			"productTypeName": "补水",
			"specificationsCount": 30,
			"specificationsUnitName": "克",
			"stockCount": 0,
			"safeCount": 0,
			"salePrice": "428",
			"productOrigin": "纤体",
			"isOnline": 0,
			"isSync": 1,
			"isOnlineStr": 'null',
			"remark": ""
		}, {
			"id": "1212ae23e92d4648a8842ea61a28397a",
			"code": "K007",
			"name": "悦颜柔肤蛋白乳液",
			"productUnitName": "瓶",
			"productUnitId": 0,
			"productTypeName": "补水",
			"specificationsCount": 30,
			"specificationsUnitName": "毫升",
			"stockCount": 0,
			"safeCount": 0,
			"salePrice": "398",
			"productOrigin": "纤体",
			"isOnline": 0,
			"isSync": 1,
			"isOnlineStr": 'null',
			"remark": ""
		}, {
			"id": "1457c185d84348219dec1cefb66f4ace",
			"code": "LS010",
			"name": "臻皙透亮精华液",
			"productUnitName": "瓶",
			"productUnitId": 0,
			"productTypeName": "补水",
			"specificationsCount": 30,
			"specificationsUnitName": "毫升",
			"stockCount": 0,
			"safeCount": 0,
			"salePrice": "268",
			"productOrigin": "纤体",
			"isOnline": 0,
			"isSync": 1,
			"isOnlineStr": 'null',
			"remark": ""
		}, {
			"id": "164c8f38db464bcfa5a8466cdf508193",
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
		}, {
			"id": "177d21debb8e4b07ad075397f8c12892",
			"code": "LS006",
			"name": "微肌修护舒缓水",
			"productUnitName": "瓶",
			"productUnitId": 0,
			"productTypeName": "修复",
			"specificationsCount": 120,
			"specificationsUnitName": "毫升",
			"stockCount": 0,
			"safeCount": 0,
			"salePrice": "238",
			"productOrigin": "纤体",
			"isOnline": 0,
			"isSync": 1,
			"isOnlineStr": 'null',
			"remark": ""
		}, {
			"id": "1b4c122cf1b64acd81bb71a01b1620eb",
			"code": "K018",
			"name": "悦颜豆蔻粉粒水",
			"productUnitName": "瓶",
			"productUnitId": 0,
			"productTypeName": "修复",
			"specificationsCount": 20,
			"specificationsUnitName": "毫升",
			"stockCount": 0,
			"safeCount": 0,
			"salePrice": "398",
			"productOrigin": "纤体",
			"isOnline": 0,
			"isSync": 1,
			"isOnlineStr": 'null',
			"remark": ""
		}],
		"totalCount": 51,
		"totalPages": 6,
		"onlineCount": 2,
		"offlineCount": 49,
		"lessCount": 0
	}
}
json=random.sample(data['data']['data'],1)
for a in json:
    shuju={'id':a['id'],'name':a['name'],'code':a['code']}
print(shuju)
#查接口产生,或者数据库查询
value_list=['fangjunjie','ceshibu','18']
#人工维护
key_list=['name','department','age']
#替换的body
str="{'name':'$name','department':'$department','age':'$age'}"
for i in range(len(key_list)):
	str=str.replace('$'+key_list[i],value_list[i])
print(str)

