# -*- coding: utf-8 -*-
# @Author       :junjie
# @Time         :2019/6/5 17:15
# @FileName     :lexuan_views.py
#IDE            :PyCharm
from flask import request, jsonify
from MPM_Mall import app, db
from models.models_lexuan import HappyUser, HappyProfitLog, ShopUserIncomeDetail


# 用户等级
userName = {
    0: "普通用户",
    1: "会员",
    2: "创客",
    3: "金牌",
    4: "联创",
    5: "总公司",
}


# 收益类型
type = {
    190: '差价',
    141: '联创一代',
    142: '联创二代',
    132: '金牌二级奖励',
    131: '金牌一级奖励',
    122: '创客二级奖励',
    121: '创客一级奖励',
    201: '包年一代奖励',
    202: '包年二代奖励',
    323: '创客推荐金牌',
    324: '创客推荐联创'
}

income_type = {
    1: '商品销售奖励',
    2: '团长奖励',
    3: '培训奖励',
    4: '团队业绩奖励',
    5: '个人业绩奖励',
    6: '充值',
    7: '调账',
    8: '提现',
    9: '省钱',
    10: '余额支付'
}

profit_type = {
    1: '商品差价奖励',
    2: '创客一级奖励',
    3: '创客二级奖励',
    4: '金牌一级奖励',
    5: '金牌二级奖励',
    6: '联创一级奖励',
    7: '联创二级奖励',
    8: '包年一级奖励',
    9: '包年二级奖励',
    10: '创客培训金牌',
    11: '创客培训联创',
    12: '团队业绩奖励',
    13: '个人业绩奖励',
    14: '充值',
    15: '调账',
    16: '提现',
    17: '省钱',
    18: '余额支付'
}

stat_type = {
    0: '在途收益',
    1: '累计收益',
    2: '临时收益'
}

# 查询关系
@app.route('/lexuan/getName', methods=['POST', 'GET'])
def api_lexuan():
    try:
        if request.method == 'POST':
            id = int(request.form['id'])
            ids = []
            id_user = HappyUser.query.get(id)
            str1 = userName[id_user.level]
            ids.append({'user_id': id,
                        'level': str1,
                        'mobile': id_user.mobile,
                        'invitecode': id_user.invite_code})
            # ids.append({'user_id': id, 'level': str1})
            while True:
                pid = HappyUser.query.get(id).invite_up_id
                pid_user = HappyUser.query.get(pid)
                str2 = userName[pid_user.level]
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
@app.route('/lexuan/getLevel', methods=['POST', 'GET'])
def lexuan_level():
    try:
        if request.method == 'POST':
            id = request.form.get("id")
            level = request.form.get("level")
            ids = []
            if level is None:
                query = HappyUser.query.filter(HappyUser.invite_up_id == id)
            else:
                query = HappyUser.query.filter(
                    HappyUser.invite_up_id == id, HappyUser.level == level)
            count = query.count()
            for ll in query.all():
                str1 = userName[ll.level]
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
@app.route('/lexuan/getIncome', methods=['POST', 'GET'])
def lexuan_go_income():
    try:
        if request.method == 'POST':
            Sum = 0
            ids = []
            orderNo = request.form['orderNo']
            query = HappyUser.query.join(
                HappyProfitLog,
                HappyUser.id == HappyProfitLog.user_id).add_entity(HappyProfitLog).filter(
                HappyProfitLog.order_no == orderNo).order_by(
                HappyProfitLog.id.asc())
            for ll in query.all():
                Sum += ll.HappyProfitLog.amount
                str1 = userName[ll.HappyUser.level]
                ids.append({'use_id': ll.HappyUser.id,
                            'mobile': ll.HappyUser.mobile,
                            'level': str1,
                            'income': str(ll.HappyProfitLog.amount),
                            'incomeType': type[ll.HappyProfitLog.profit_type]})
            return jsonify({'msg': '成功', 'code': 200, 'data': {
                           'count': str(Sum), 'items': ids}})
    except Exception as exception:
        print(str(exception))
        return jsonify({'msg': '系统错误', 'code': 500, 'error': str(exception)})


# 查询收益
@app.route('/lexuan/getIncome1', methods=['POST', 'GET'])
def lexuan_java_income():
    try:
        if request.method == 'POST':
            Sum = 0
            ids = []
            orderNo = request.form['orderNo']
            query = HappyUser.query.join(
                ShopUserIncomeDetail,
                HappyUser.id == ShopUserIncomeDetail.user_id).add_entity(ShopUserIncomeDetail).filter(
                ShopUserIncomeDetail.order_no == orderNo).order_by(
                ShopUserIncomeDetail.id.asc())
            for ll in query.all():
                if ll.ShopUserIncomeDetail.operate_type == 1:
                    Sum += ll.ShopUserIncomeDetail.operate_income
                    price = str(ll.ShopUserIncomeDetail.operate_income)
                else:
                    Sum -= ll.ShopUserIncomeDetail.operate_income
                    price = "-" + str(ll.ShopUserIncomeDetail.operate_income)

                ids.append({'use_id': ll.HappyUser.id,
                            'level': userName[ll.HappyUser.level],
                            'IncomeDetail': price,
                            'mobile': ll.HappyUser.mobile,
                            'stat_type': stat_type[ll.ShopUserIncomeDetail.stat_type],
                            'profit_type': profit_type[ll.ShopUserIncomeDetail.profit_type],
                            'incometype': income_type[ll.ShopUserIncomeDetail.income_type]})
            return jsonify({'msg': '成功', 'code': 200, 'data': {
                           'count': str(Sum), 'items': ids}})
    except Exception as exception:
        print(str(exception))
        return jsonify({'msg': '系统错误', 'code': 500, 'error': str(exception)})
