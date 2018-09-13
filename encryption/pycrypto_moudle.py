#pip install pycryptodome
from Crypto.Cipher import AES
import base64

#将str类型转成byte类型
def add_to_16(value):
    while len(value) % 16 != 0:
        value += '\0'
    print(str.encode(value))
    return str.encode(value)

#加密过程 secret_key:秘钥 encrypt_str：需要加密的字符串
def encrypt_method(secret_key,encrypt_str):
    aes = AES.new(add_to_16(secret_key), AES.MODE_ECB)#初始化加密器
    encrypt_aes = aes.encrypt(add_to_16(encrypt_str))#进行aes加密
    #进行base64加密，并将aes加密后的 byte 转成 str类型
    return str(base64.encodebytes(encrypt_aes),encoding='utf-8')


#加密过程 secret_key:秘钥 decrypt_str：需要解密的字符串
def decrypt_method(secret_key,decrypt_str):
    aes = AES.new(add_to_16(secret_key), AES.MODE_ECB)#初始化化加密器
    #base 解密成 byte的类型
    decrypt_byte = base64.decodebytes(decrypt_str.encode(encoding='utf-8'))
    #des 秘钥解密 返回string
    return str(aes.decrypt(decrypt_byte),encoding='utf-8').replace('\0','')

key = '123478'
print(encrypt_method(key,'root@123'))
print(decrypt_method(key,'GtgA3tg2mCLyQo+jATSlDQ=='))