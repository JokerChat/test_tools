# -*- coding: utf-8 -*-
# @Author       :junjie    
# @Time         :2020/5/22 11:29
# @FileName     :rsa_code.py
# @Motto        :AS the tree,so the fruit
#IDE            :PyCharm

import rsa

import base64

from public.config_path import PUBLIC_FILE_PATH,PRIVATE_FILE_PATH

class HandleSign:

    @classmethod
    def to_encrypt(cls, msg, pub_key=None):
        """
        非对称加密
        :param msg: 待加密字符串或者字节
        :param pub_key: 公钥
        :return: 密文
        """
        if isinstance(msg, str):            # 如果msg为字符串, 则转化为字节类型
            msg = msg.encode('utf-8')
        elif isinstance(msg, bytes):        # 如果msg为字节类型, 则无需处理
            pass
        else:                               # 否则抛出异常
            raise TypeError('msg必须为字符串或者字节类型!')

        if not pub_key:                     # 如果pub_key为空, 则使用全局公钥
            with open(PUBLIC_FILE_PATH, 'rb') as file:   # 读取公钥
                pub_key = file.read()

        elif isinstance(pub_key, str):      # 如果pub_key为字符串, 则转化为字节类型
            pub_key = pub_key.encode('utf-8')
        elif isinstance(pub_key, bytes):    # 如果msg为字节类型, 则无需处理
            pass
        else:                               # 否则抛出异常
            raise TypeError('pub_key必须为None、字符串或者字节类型!')
        #后端开发密钥格式为pkcs8格式公钥，'-----BEGIN PUBLIC KEY-----' 用load_pkcs1_openssl_pem()这个方法
        #pkcs1格式公钥用load_pkcs1()这个方法
        public_key_obj = rsa.PublicKey.load_pkcs1_openssl_pem(pub_key)  # 创建 PublicKey 对象

        cryto_msg = rsa.encrypt(msg, public_key_obj)  # 生成加密文本
        cipher_base64 = base64.b64encode(cryto_msg)   # 将加密文本转化为 base64 编码

        return cipher_base64.decode()   # 将字节类型的 base64 编码转化为字符串类型


    @classmethod
    def to_decrypt(cls, msg, pri_key=None):  # 用私钥解密
        if isinstance(msg, str):  # 如果msg为字符串, 则转化为字节类型
            msg = msg.encode('utf-8')
        elif isinstance(msg, bytes):  # 如果msg为字节类型, 则无需处理
            pass
        else:  # 否则抛出异常
            raise TypeError('msg必须为字符串或者字节类型!')

        if not pri_key:  # 如果pub_key为空, 则使用全局公钥
            with open(PRIVATE_FILE_PATH, 'rb') as file:  # 读取公钥
                pri_key = file.read()

        elif isinstance(pri_key, str):  # 如果pub_key为字符串, 则转化为字节类型
            pri_key = pri_key.encode('utf-8')
        elif isinstance(pri_key, bytes):  # 如果msg为字节类型, 则无需处理
            pass
        else:  # 否则抛出异常
            raise TypeError('pub_key必须为None、字符串或者字节类型!')
            # python只支持pkcs1格式的私钥解密，需要使用openssl将pkcs8转为pkcs1格式
        #https://blog.csdn.net/sanpangouba/article/details/100997735
        privateKey_key_obj = rsa.PrivateKey.load_pkcs1(pri_key)  # 创建 PublicKey 对象

        msg=base64.b64decode(msg) #base64 解码

        decrypt_msg = rsa.decrypt(msg, privateKey_key_obj)  # 生成加密文本

        return decrypt_msg.decode('utf-8')  # 将字节类型的文本转化为字符串类型

    @classmethod
    def create_keys(cls):  # 生成公钥和私钥
        # 设置1024位长度
        (pubkey, privkey) = rsa.newkeys(1024)
        #密钥格式为pkcs1格式, -----BEGIN RSA PUBLIC KEY-----
        pub = pubkey.save_pkcs1()
        with open(PUBLIC_FILE_PATH, 'wb+')as f:
            f.write(pub)
        pri = privkey.save_pkcs1()
        with open(PRIVATE_FILE_PATH, 'wb+')as f:
            f.write(pri)

    @classmethod
    def generate_sign(cls, message):
        """
        生成sign
        :param message: message, 代加密内容, 为str类型
        :return: 加密后字符串
        """
        sign = cls.to_encrypt(message)  # 生成sign
        return sign

    @classmethod
    def decrypt_sign(cls,message):
        """
        解密sign
        :param message: message, 加密内容, 为str类型
        :return: 解密后字符串
        """
        sign = cls.to_decrypt(message)  # 解密sign
        return sign




if __name__ == '__main__':
    to_msg='ZcULYuVHhti4grRNQ0TtAZ8IDses7eAH/DTVx8eK+eRzsboRhhJj0tRlvnNjw1kKaSx9HdAq9eRI9b7AGnfsmCLp83mxkTeH6fV6BFPv6/klcl0/QURivLZ6fGn9U4iX5foDggPfUXFD4369IEVoCm+rz4OchtZBuUR9H/vupBY='
    new_msg=HandleSign.decrypt_sign(to_msg)
    print(new_msg)
    msg='abc'
    aaaa=HandleSign.generate_sign(msg)
    print(aaaa)
