# -*- coding: utf-8 -*-
# @Author       :junjie
# @Time         :2019/6/5 17:15
# @FileName     :views.py
#IDE            :PyCharm
from flask import request, jsonify
from zhuan_bo import app, db
from models.mpm import ShopUser, ShopUserInvite, ShopUserIncomeDetail, ShopOrder
from models.models_zhuanbo import MliveProfitLog,MliveUser
from public.aescode import AES_CBC
from MPM_Mall.get_requests import getRequests
aes = AES_CBC()

userName = {0: "普通用户",
            1: "VIP",
            2: "店长",
            3: "总监",
            4: "合伙人",
            5: "联创",
            6:"总公司"}
# 收益类型：面膜销售：差价 190；全部返还 180；拉新给予 171  （+10）；拉新扣减 172 （ -10）；；；服务投资：差价 290；全部返还 280；越级奖励 270；一代 211；二代 212；
profit_type={
    141:'下级运费扣减',
    151:'面膜销售一代联创',
    152:'面膜销售一代联创',
    160:'面膜订单进货差价',
    260:'套餐订单进货差价',
    190:'面膜销售差价',
    180:'面膜全部返还',
    171:'拉新给10块',
    172:'拉新扣减10块',
    290:'服务商投资差价',
    280:'服务商全部返还',
    270:'服务商越级奖励',
    211:'服务商一代奖励',
    212:'服务商二代奖励',
    213:'服务商三代奖励',
    251:'联创第一代',
    252:'联创第二代',
    360:'身份奖励'
}
# 查询关系
@app.route('/getName', methods=['POST', 'GET'])
def apiName():
    try:
        if request.method == 'POST':
            id = int(request.form['id'])
            ids = []
            id_user = ShopUser.query.get(id)
            str1 = userName[id_user.pt_level]
            ids.append({'user_id': id,
                        'level': str1,
                        'mobile': id_user.mobile,
                        'invitecode': id_user.invite_code})
            # ids.append({'user_id': id, 'level': str1})
            while True:
                pid = ShopUserInvite.query.get(id).pid
                pid_user = ShopUser.query.get(pid)
                str2 = userName[pid_user.pt_level]
                ids.append({'user_id': pid,
                            'level': str2,
                            'mobile': pid_user.mobile,
                            'invitecode': pid_user.invite_code})
                # ids.append({'user_id': pid, 'level': str2})
                id = pid
                if pid == 1:
                    break
            return jsonify({'msg': '成功', 'code': 200, 'data': {'items': ids}})
        else:
            return jsonify({
                'msg': "该接口仅支持 [POST] 请求方式",
                'code': 202
            })
    except Exception as exception:
        print(str(exception))
        return jsonify({'msg': '系统错误', 'code': 500})

# 查询下级身份
@app.route('/getLevel', methods=['POST', 'GET'])
def apiLevel():
    try:
        if request.method == 'POST':
            id = request.form.get("id")
            level = request.form.get("level")
            ids = []
            if level is None:
                query = ShopUser.query.join(
                    ShopUserInvite,
                    ShopUserInvite.id == ShopUser.id).filter(
                    ShopUserInvite.pid == id)
            else:
                query = ShopUser.query.join(
                    ShopUserInvite, ShopUserInvite.id == ShopUser.id).filter(
                    ShopUserInvite.pid == id, ShopUser.pt_level == level)
            count = query.count()
            for ll in query.all():
                str1 = userName[ll.pt_level]
                ids.append({'user_id': ll.id, 'level': str1,
                            'mobile': ll.mobile, 'invitecode': ll.invite_code})
            return jsonify({'msg': '成功', 'code': 200, 'data': {
                           'total': count, 'items': ids}})
        else:
            return jsonify({
                'msg': "该接口仅支持 [POST] 请求方式",
                'code': 202
            })
    except Exception as exception:
        print(str(exception))
        return jsonify({'msg': '系统错误', 'code': 500})


# 查询收益
@app.route('/getIncome', methods=['POST', 'GET'])
def apiIncome():
    try:
        if request.method == 'POST':
            Sum = 0
            ids = []
            orderNo = request.form['orderNo']
            query = MliveUser.query.join(
                MliveProfitLog,
                MliveUser.id == MliveProfitLog.user_id).add_entity(MliveProfitLog).filter(
                MliveProfitLog.order_no == orderNo).order_by(
                MliveProfitLog.id.asc())
            for ll in query.all():
                Sum += ll.MliveProfitLog.amount
                str1 = userName[ll.MliveUser.level]
                ids.append({'use_id': ll.MliveUser.id, 'mobile':ll.MliveUser.mobile,'level': str1, 'income': str(
                    ll.MliveProfitLog.amount),'incomeType':profit_type[ll.MliveProfitLog.profit_type]})
            return jsonify({'msg': '成功', 'code': 200, 'data': {
                           'count': str(Sum), 'items': ids}})
    except Exception as exception:
        print(str(exception))
        return jsonify({'msg': '系统错误', 'code': 500, 'error': str(exception)})

# AES加解密
@app.route('/aescoder', methods=['POST', 'GET'])
def apiEncode():
    try:
        if request.method == 'POST':
            text = request.form['text']
            type = int(request.form['type'])
            if type == 0:
                aes_text = aes.encrypt_oracle(text)
                return jsonify({'msg': '成功', 'code': 200, 'data': aes_text})
            elif type == 1:
                aes_text = aes.decrypt_oralce(text)
                return jsonify({'msg': '成功', 'code': 200, 'data': aes_text})
    except Exception as exception:
        return jsonify({'msg': '系统错误', 'code': 500, 'error': str(exception)})

 # 订单修改


@app.route('/apiOrder', methods=['POST', 'GET'])
def apiOrder():
    try:
        if request.method == 'POST':
            orderNo = request.form['orderNo']
            sql = f'SELECT a.profit_type,a.amount,a.user_id,b.mobile,b.level FROM mlive_profit_log a JOIN mlive_user b ON a.user_id=b.id WHERE order_no={orderNo} ORDER BY a.id ASC'
            income_data = db.session.execute(sql)
            print(list(income_data.fetchall()))
            return jsonify({'msg': '修改成功', 'code': 200, })
        elif request.method == 'GET':
            pass
    except Exception as exception:
        return jsonify({'msg': '系统错误', 'code': 500, 'error': str(exception)})


# 注册
@app.route('/register', methods=['POST', 'GET'])
def apiregister():
    try:
        if request.method == 'POST':
            mobile = int(request.form['mobile'])
            inviteCode = request.form['inviteCode']
            number=int(request.form['number'])
            url1 = 'auth/code'
            url2 = 'auth/login/mp'
            index = 0
            while True:
                data1 = {
                    "type": 1,
                    "areaCode": "86",
                    "mobile": str(mobile),
                    "mercId": "888000000000004",
                    "platform": "ZBMALL",
                    "sysCnl": "H5",
                    "timestamp": "1574066250"
                }
                if index == number:
                    break
                getRequests(url1, data1).get_requests()
                data2 = {
                    "code": "0",
                    "mobile": str(mobile),
                    "inviteCode": inviteCode,
                    "mercId": "888000000000004",
                    "platform": "ZBMALL",
                    "sysCnl": "H5",
                    "timestamp": "1574066264"
                }
                new_inviteCode = getRequests(url2, data2).get_requests()['data']['inviteCode']
                inviteCode = new_inviteCode
                mobile += 1
                index += 1
        return jsonify({'msg': '成功', 'code': 200, 'data': '注册成功'})
    except Exception as exception:
        return jsonify({'msg': '系统错误', 'code': 500, 'error': str(exception)})
