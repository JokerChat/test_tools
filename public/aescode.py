# coding=utf-8
# AES AES/CBC/PKCS5|Zero

import base64
from Crypto.Cipher import AES
from public.config import *
key=get('aes')['key'][get('is_test')]
iv=get('aes')['iv'][get('is_test')]
class AES_CBC:

    def add_to_16(self, value):
        while len(value) % 16 != 0:
            value += '\0'
        return str.encode(value)  # 返回bytes

    # 加密方法
    def encrypt_oracle(self,  text):
        # 初始化加密器
        aes = AES.new(self.add_to_16(key), AES.MODE_CBC, self.add_to_16(iv))
        bs = AES.block_size
        pad2 = lambda s: s + (bs - len(s) % bs) * chr(bs - len(s) % bs)  # PKS7

        encrypt_aes = aes.encrypt(str.encode(pad2(text)))

        # 用base64转成字符串形式
        # 执行加密并转码返回bytes
        encrypted_text = str(base64.encodebytes(encrypt_aes), encoding='utf-8')
        # 和js的 结果相同 http://tool.chacuo.net/cryptaes
        return encrypted_text.replace('\n','') #去除换行符

    # 解密方法
    def decrypt_oralce(self, text):
        # 初始化加密器
        # 偏移量 16个0
        iv = "dMbtHORyqseYwE0o"
        aes = AES.new(self.add_to_16(key), AES.MODE_CBC, self.add_to_16(iv))
        # 优先逆向解密base64成bytes
        base64_decrypted = base64.decodebytes(text.encode(encoding='utf-8'))
        # 执行解密密并转码返回str
        decrypted_text = str(aes.decrypt(base64_decrypted), encoding='utf-8')
        unpad = lambda s: s[0:-ord(s[-1])]
        return unpad(decrypted_text)


if __name__ == '__main__':
    aes = AES_CBC()
    enc_text = aes.encrypt_oracle("AES")
    # 解密
    dec_text = aes.decrypt_oralce('tcm+BCxtWowWVl0Awa1pOPQjr329h1rw/9wER+krASE=')
    print(enc_text)
    print(dec_text)
