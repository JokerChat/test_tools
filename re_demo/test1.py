# -*- coding: utf-8 -*-
# @Author       :junjie    
# @Time         :2019/12/17 20:53
# @FileName     :test1.py
#IDE            :PyCharm
import json

def dict_generator(indict, pre=None):
    pre = pre[:] if pre else []
    if isinstance(indict, dict):
        for key, value in indict.items():
            if isinstance(value, dict) :
                if len(value) == 0: #如果值为空
                    yield pre+[key, '{}'] #jsonPath加上空字典
                else: #如果值不为空则需要继续迭代
                    for d in dict_generator(value, pre + [key]):
                        yield d
            elif isinstance(value, list) and key != "附录（通话号码列列表）数据节点": #这个太长先不要
                if len(value) == 0:
                    yield pre+[key, '[]']
                else:
                    for v in value: #把列表中的元素拿出来迭代
                        for d in dict_generator(v, pre + [key]):
                            yield d
            elif isinstance(value, tuple):
                if len(value) == 0:
                    yield pre+[key, '()']
                else:
                    for v in value:
                        for d in dict_generator(v, pre + [key]):
                            yield d
            else: #如果不是'值'不是元组,列表,字典则输出结果
                yield pre + [key, value]
#     elif isinstance(indict, list):
    else:
        yield pre + [indict]

if __name__ == "__main__":
    sJSON = '{"a":1}' #可以弄复杂的json对象
    sValue ={"msg":"成功","code":10000,"data":{"total":1,"items":[{"id":"1","nickname":"","teamNumber":215545,"ptLevel":7,"pid":"1","mobile":"","status":1,"children":[{"id":"863","nickname":"李玉琴","teamNumber":2182,"ptLevel":6,"pid":"863","mobile":"13732437333","status":1,"children":[{"id":"871","nickname":"胡生琼","teamNumber":1151,"ptLevel":5,"pid":"871","mobile":"18166013079","status":1,"children":[{"id":"882","nickname":"补秀兰","teamNumber":332,"ptLevel":5,"pid":"882","mobile":"13368183631","status":1,"children":[{"id":"8563","nickname":"郑能巧","teamNumber":58,"ptLevel":3,"pid":"8563","mobile":"15310098998","status":1,"children":[{"id":"49069","nickname":"肖春红","teamNumber":26,"ptLevel":3,"pid":"49069","mobile":"18184785477","status":1,"children":[{"id":"79891","nickname":"陈春梅","teamNumber":1,"ptLevel":2,"pid":"49069","mobile":"13718976532","status":1,"children":[],"teamNumberHY":1,"teamDirectNumber":1,"authNo":"B77937","wxNo":"","inviteNo":"B77937","upGradeTime":"2018-12-07 20:13"}],"teamNumberHY":26,"teamDirectNumber":21,"authNo":"B48950","wxNo":"","inviteNo":"","upGradeTime":""}],"teamNumberHY":58,"teamDirectNumber":3,"authNo":"B8552","wxNo":"qiaoqiao-208","inviteNo":"B8552","upGradeTime":"2017-10-10 13:44"}],"teamNumberHY":332,"teamDirectNumber":43,"authNo":"B871","wxNo":"m13368163631","inviteNo":"B871","upGradeTime":"2017-10-07 16:56"}],"teamNumberHY":1151,"teamDirectNumber":26,"authNo":"B860","wxNo":"18166013079","inviteNo":"B860","upGradeTime":"2017-10-07 16:31"}],"teamNumberHY":2182,"teamDirectNumber":15,"authNo":"B852","wxNo":"390858364","inviteNo":"B852","upGradeTime":"2017-10-07 16:04"}],"teamNumberHY":215545,"teamDirectNumber":65,"authNo":"","wxNo":"","inviteNo":"","upGradeTime":"2019-11-14 21:49"}]}}
    for i in dict_generator(sValue):
        print('.'.join(i[0:-1]), ':', i[-1])