# -*- coding: utf-8 -*-
# @Author       :junjie
# @Time         :2019/6/5 17:15
# @FileName     :lexuan_views.py
#IDE            :PyCharm
from flask import request, jsonify
from MPM_Mall import app,db
from MPM_Mall.MPM_sign import checkSign
from models.mpm import ShopUser, ShopUserInvite, ShopUserIncomeDetail,ShopOrder
from public.aescode import AES_CBC
from MPM_Mall.handle_requests import HandleRequests
from public.rsa_code import HandleSign
from public.api_common import project_type
aes = AES_CBC()
# 签名数据生成接口
@app.route('/sign', methods=['GET', 'POST'])
def apiSign():
    try:
        if request.method == 'POST':
            data = request.get_json()
            if data is None:
                return jsonify({'code': 202, 'msg': '参数必须为json格式'})
            else:
                sign = checkSign(data).check_dict()
                if project_type == 3:
                    return jsonify({'code': 200,
                                'get_sign': sign['X-Sign'],
                                'msg': '成功'
                                    })
                else:
                    return jsonify({'code': 200,
                                    'get_sign': sign['X-MPMALL-Sign'],
                                    'msg': '成功'
                                    })
        else:
            return jsonify({
                'msg': "该接口仅支持 [POST] 请求方式",
                "code": 201
            })
    except Exception as exception:
        print(str(exception))
        return jsonify({'code': 500, 'msg': '系统错误'})

#
# def userName(level):
#     if level == 0:
#         str1 = 'M星人'
#     elif level == 1:
#         str1 = 'M达人'
#     elif level == 2:
#         str1 = 'M体验官'
#     elif level == 3:
#         str1 = 'M司令'
#     elif level == 4:
#         str1 = '合伙人'
#     elif level == 5:
#         str1 = '高级合伙人'
#     elif level == 6:
#         str1 = '总监'
#     elif level == 7:
#         str1 = '高级总监'
#     elif level == 8:
#         str1 = '代言人'
#     else:
#         str1 = '高级代言人'
#     return str1


# def userName(level):
#     if level == 0:
#         str1 = '普通用户'
#     elif level == 1:
#         str1 = 'VIP'
#     elif level == 2:
#         str1 = '店长'
#     elif level == 3:
#         str1 = '总监'
#     elif level == 4:
#         str1 = '合伙人'
#     elif level == 5:
#         str1 = '联创'
#     else:
#         str1 = '总公司'
#     return str1


def userName(level):
    if level == 0:
        str1 = '普通用户'
    elif level == 1:
        str1 = '会员'
    elif level == 2:
        str1 = '创客'
    elif level ==3:
        str1 = '金牌'
    elif level ==4:
        str1='联创'
    else:
        str1='总公司'
    return str1

# 查询关系
@app.route('/getName', methods=['POST', 'GET'])
def apiName():
    try:
        if request.method == 'POST':
            id = int(request.form['id'])
            ids = []
            id_user = ShopUser.query.get(id)
            str1 = userName(id_user.pt_level)
            ids.append({'user_id': id,
                        'level': str1,
                        'mobile': id_user.mobile,
                        # 'invitecode': id_user.invite_code
                        })
            # ids.append({'user_id': id, 'level': str1})
            while True:
                pid = ShopUserInvite.query.get(id).pid
                pid_user = ShopUser.query.get(pid)
                str2 = userName(pid_user.pt_level)
                ids.append({'user_id': pid,
                            'level': str2,
                            'mobile': pid_user.mobile,
                            # 'invitecode': pid_user.invite_code
                            })
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
                str1 = userName(ll.pt_level)
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

# income_type={
#             1 :"商品销售奖励",
#             2 :"服务商销售奖励",
#             3: "下级销售奖励",
#             4: "提现",
#             5:"进货差价奖励"
#
# }



income_type={
    1:"一代奖励",
    2:"二代奖励",
    3:"越级奖励",
    4:"金钻奖励",
    5:"一代奖励扣减",
    6:"下级进货差价奖励",
    7:"提现",
    8:"保证金",
    9:"礼包活动",
    10:"促销活动"


}
# 查询收益
@app.route('/getIncome', methods=['POST', 'GET'])
def apiIncome():
    try:
        if request.method == 'POST':
            Sum = 0
            ids = []
            orderNo = request.form['orderNo']
            query = ShopUser.query.join(
                ShopUserIncomeDetail,
                ShopUser.id == ShopUserIncomeDetail.user_id).add_entity(ShopUserIncomeDetail).filter(
                ShopUserIncomeDetail.order_no == orderNo).order_by(
                ShopUserIncomeDetail.id.asc())
            for ll in query.all():
                if ll.ShopUserIncomeDetail.operate_type== 1:
                    Sum += ll.ShopUserIncomeDetail.operate_income
                    price=str(ll.ShopUserIncomeDetail.operate_income)
                else:
                    Sum -= ll.ShopUserIncomeDetail.operate_income
                    price = "-"+str(ll.ShopUserIncomeDetail.operate_income)
                str1 = userName(ll.ShopUser.pt_level)
                ids.append({'use_id': ll.ShopUser.id, 'level': str1, 'IncomeDetail': price,'mobile':ll.ShopUser.mobile,'incometype':income_type[ll.ShopUserIncomeDetail.income_type]})
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
            text = str(request.form['text'])
            type = int(request.form['type'])
            # 0 加密 1 解密
            if type == 0:
                aes_text = aes.encrypt_oracle(text)
                return jsonify({'msg': '成功', 'code': 200, 'data': aes_text})
            elif type == 1:
                aes_text = aes.decrypt_oralce(text)
                return jsonify({'msg': '成功', 'code': 200, 'data': aes_text})
    except Exception as exception:
        return jsonify({'msg': '系统错误', 'code': 500, 'error': str(exception)})



#RSA加解密
@app.route('/rsacoder', methods=['POST', 'GET'])
def api_rsa_code():
    try:
        if request.method == 'POST':
            text = str(request.form['text'])
            type = int(request.form['type'])
            # 0 加密 1 解密
            if type == 0:
                aes_text = HandleSign.generate_sign(text)
                return jsonify({'msg': '成功', 'code': 200, 'data': aes_text})
            elif type == 1:
                aes_text = HandleSign.decrypt_sign(text)
                return jsonify({'msg': '成功', 'code': 200, 'data': aes_text})
    except Exception as exception:
        return jsonify({'msg': '系统错误', 'code': 500, 'error': str(exception)})



 #订单修改
@app.route('/apiOrder', methods=['POST', 'GET'])
def apiOrder():
    try:
        if request.method == 'POST':
            orderNo = request.form['orderNo']
            sql=f'UPDATE shop_order SET price=0.01 WHERE order_no={ orderNo }'
            try:
                db.session.execute(sql)
            except Exception as exception:
                print(exception)
            return jsonify({'msg': '修改成功', 'code': 200,})
        elif request.method == 'GET':
            orderNo = request.args.get('orderNo')
            sql = f'UPDATE shop_order SET price=0.01 WHERE order_no={orderNo}'
            try:
                db.session.execute(sql)
            except Exception as exception:
                print(exception)
            return jsonify({'msg': '修改成功', 'code': 200, })
    except Exception as exception:
        return jsonify({'msg': '系统错误', 'code': 500, 'error': str(exception)})

# 封装接口请求,不用进行接口验签
do_request = HandleRequests()
@app.route('/api', methods=['POST', 'GET'])
def apirequest():
    try:
        if request.method == 'POST':
            data = request.get_json()
            url=data['url']
            json_data=data['data']
            if 'token' in data:
                token=data['token']
                if project_type == 3:
                    do_request.add_header({'X-Token':token})
                else:
                    do_request.add_header({'X-MPMALL-Token': token})
            res=do_request.send("POST", url, json=json_data)
            return jsonify(res.json())
    except Exception as exception:
        return jsonify({'msg': '系统错误', 'code': 500, 'error': str(exception)})