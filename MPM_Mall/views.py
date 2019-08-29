# -*- coding: utf-8 -*-
# @Author       :junjie    
# @Time         :2019/6/5 17:15
# @FileName     :views.py
#IDE            :PyCharm
from flask import request,jsonify
from MPM_Mall import app
from MPM_Mall.MPM_sign import checkSign
from models.mpm import ShopUser,ShopUserInvite


#签名数据生成接口
@app.route('/sign',methods=['GET','POST'])
def apiSign():
    try:
        if request.method=='POST':
            data=request.get_json()
            if data is None:
                return jsonify({'code':202,'msg':'参数必须为json格式'})
            else:
                sign = checkSign(data).check_dict()
                return jsonify({'code':200,
                                'get_sign':sign,
                                'msg':'成功'
                                })
        else:
            return jsonify({
                    'msg': "该接口仅支持 [POST] 请求方式",
                    "code": 201
                        })
    except Exception as exception:
        print(str(exception))
        return jsonify({'code': 500, 'msg': '系统错误'})


def userName(level):
    if level == 0:
        str1 = 'M星人'
    elif level == 1:
        str1 = 'M达人'
    elif level == 2:
        str1 = 'M体验官'
    elif level ==3:
        str1 = 'M司令'
    elif level ==4:
        str1='合伙人'
    elif level ==5:
        str1='高级合伙人'
    elif level ==6:
        str1='总监'
    elif level ==7:
        str1='高级总监'
    elif level ==8:
        str1='代言人'
    else:
        str1='高级代言人'
    return str1


#查询关系
@app.route('/getName',methods=['POST','GET'])
def apiName():
    try:
        if request.method == 'POST':
            id = int(request.form['id'])
            ids = []
            id_user=ShopUser.query.get(id)
            str1 = userName(id_user.pt_level)
            ids.append({'user_id':id,'level':str1,'mobile':id_user.mobile,'invitecode':id_user.invite_code})
            while True:
                pid=ShopUserInvite.query.get(id).pid
                pid_user=ShopUser.query.get(pid)
                str2=userName(pid_user.pt_level)
                ids.append({'user_id':pid,'level':str2,'mobile':pid_user.mobile,'invitecode':pid_user.invite_code})
                id=pid
                if pid==1:
                    break
            return jsonify({'msg':'成功','code':200,'data':{'items':ids}})
        else:
            return jsonify({
                'msg': "该接口仅支持 [POST] 请求方式",
                'code': 202
            })
    except Exception as exception:
        print(str(exception))
        return jsonify({'msg': '系统错误','code': 500})

#查询下级身份
@app.route('/getLevel',methods=['POST','GET'])
def apiLevel():
    try:
        if request.method == 'POST':
            id = request.form.get("id")
            level=request.form.get("level")
            ids = []
            if level is None:
                query=ShopUser.query.join(ShopUserInvite,ShopUserInvite.id==ShopUser.id).filter(ShopUserInvite.pid==id)
            else:
                query = ShopUser.query.join(ShopUserInvite, ShopUserInvite.id == ShopUser.id).filter(ShopUserInvite.pid == id,ShopUser.pt_level==level)
            count=query.count()
            for ll in query.all():
                str1 = userName(ll.pt_level)
                ids.append({'user_id':ll.id,'level':str1,'mobile':ll.mobile,'invitecode':ll.invite_code})
            return jsonify({'msg':'成功','code':200,'data':{'total':count,'items':ids}})
        else:
            return jsonify({
                'msg': "该接口仅支持 [POST] 请求方式",
                'code': 202
            })
    except Exception as exception:
        print(str(exception))
        return jsonify({'msg': '系统错误','code': 500 })