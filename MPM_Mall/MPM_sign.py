# -*- coding: utf-8 -*-
# @Author       :junjie
# @Time         :2019/4/22 20:37
# @FileName     :MPM_sign.py
#IDE            :PyCharm
import hashlib
import base64
from public.api_common import api_sign,project_type
from public.log import logger
# mylog=logger('验签模块').get_logger()
class checkSign:
    # 初始化传入dict
    def __init__(self, dict):
        # mylog.info(f"请求参数：{dict}")
        # 不改变传入的data=>直接对字典进行复制
        data = dict.copy()
        self.dict = data

    def check_dict(self):
        # 首先判断字典是否空,为空直接加密
        if not self.dict:
            string = ''
            if project_type != 3:
                return {"X-MPMALL-Sign": self.__sign(string)}
            else:
                return {"X-Sign": self.__sign(string)}
        else:
            # 非空字典,过滤value为空和嵌套字典、列表
            for k, v in list(self.dict.items()):
                if v == '' or v is None:
                    self.dict.pop(k)
                for k, v in list(self.dict.items()):
                    if type(
                            self.dict[k]).__name__ == 'dict'or type(
                            self.dict[k]).__name__ == 'list':
                        self.dict.pop(k)
            # 对字典进行ASCII码排序
            new_list = sorted(self.dict.items())
            alist = []
            for i in new_list:
                data = '&' + str(i[0]) + '=' + str(i[1])
                alist.append(data)
            new_string = ''.join(alist)
            if project_type != 3:
                return {"X-MPMALL-Sign": self.__sign(new_string)}
            else:
                return {"X-Sign": self.__sign(new_string)}
    # 私有方法,生成签名

    def __sign(self, string):
        if string:
            sign = string[1:] + '&key=' + api_sign  # 测试环境
            m = hashlib.md5()
            m.update(sign.encode("utf8"))
            encodeStr = m.hexdigest()
            base_code = base64.b64encode(encodeStr.encode('utf-8'))
            return str(base_code, 'utf-8')
        else:
            sign = 'key=' + api_sign
            m = hashlib.md5()
            m.update(sign.encode("utf8"))
            encodeStr = m.hexdigest()
            base_code = base64.b64encode(encodeStr.encode('utf-8'))
            return str(base_code, 'utf-8')


if __name__ == '__main__':
    dict = {
    "sysCnl": "IOS",
    "mercId": "888000000000001",
    "platform": "LXMALL",
    "timestamp": "1590458914",
    "position":9
}
    Sign = checkSign(dict)
    print(Sign.check_dict())
