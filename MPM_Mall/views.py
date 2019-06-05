# -*- coding: utf-8 -*-
# @Author       :junjie    
# @Time         :2019/6/5 17:15
# @FileName     :views.py
#IDE            :PyCharm
from flask import request,jsonify
from MPM_Mall import app
from MPM_Mall.MPM_sign import checkSign

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
    except Exception as e:
        return jsonify({'code': 500, 'msg': '系统错误'})