from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex


# 如果text不足16位的倍数就用空格补足为16位
def add_to_16(text):
    if len(text.encode('utf-8')) % 16:
        add = 16 - (len(text.encode('utf-8')) % 16)
    else:
        add = 0
    text = text + ('\0' * add)
    return text.encode('utf-8')


# 加密函数


def encrypt(text):

    key = key_input.encode('utf-8')
    mode = AES.MODE_CBC
    iv = iv_input.encode('utf-8')
    text = add_to_16(text)
    cryptos = AES.new(key, mode, iv)
    cipher_text = cryptos.encrypt(text)
    # 因为AES加密后的字符串不一定是ascii字符集的，输出保存可能存在问题，所以这里转为16进制字符串
    return b2a_hex(cipher_text)


# 解密后，去掉补足的空格用strip() 去掉
def decrypt(text):
    key = key_input.encode('utf-8')
    iv = iv_input.encode('utf-8')
    mode = AES.MODE_CBC
    cryptos = AES.new(key, mode, iv)
    plain_text = cryptos.decrypt(a2b_hex(text))
    return bytes.decode(plain_text).rstrip('\0')


if __name__ == '__main__':
# 判断语句

    answer=input('是否输入秘钥和偏移量y/n\n')
    while True:
        if answer == 'y' or answer == 'Y':
            key_input = input("请输入秘钥（长度为16位）：")
            iv_input = input("请输入偏移量iv（长度为16位）：")
            if len(key_input) % 16 ==0 and len(iv_input) % 16 == 0:
                print("输入正确")
            else:
                print("输入位数错误,请重新输入")
                continue
            text = input("请输入要加密的字符串：")
            print(text + "的AES加密结果为：",encrypt(text))
            answer = input('是否解密y/n\n')
            if answer == 'y' or answer == 'Y':
                print(str(encrypt(text)) + "的AES加密结果为：", decrypt(encrypt(text)))
            else:
                break
        else:
            key_input = "aaaaaaabbbbcccc1"
            iv_input = "1684654313456378"
            text = input("请输入要加密的字符串：")
            print(text + "的AES加密结果为：", encrypt(text))
            answer = input('是否解密y/n\n')
            if answer == 'y' or answer == 'Y':
                print(str(encrypt(text)) + "的AES加密结果为：", decrypt(encrypt(text)))
            else:
                break

# key = '9999999999999999'.encode('utf-8')
# mode = AES.MODE_CBC
# iv = b'qqqqqqqqqqqqqqqq'
#判断语句
# answer=input('是否输入秘钥和偏移量y/n\n')
# if
# key_input = input("请输入秘钥（长度为16位）：")
# iv_input = input("请输入偏移量iv（长度为16位）：")
#     e = encrypt("hello world")  # 加密
#     d = decrypt(e)  # 解密
#     print("加密:", e)
#     print("解密:", d)


# """
# ECB没有偏移量
# """
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex
def add_to_16(text):
    if len(text.encode('utf-8')) % 16:
        add = 16 - (len(text.encode('utf-8')) % 16)
    else:
        add = 0
    text = text + ('\0' * add)
    return text.encode('utf-8')

# 加密函数
def encrypt(text):
    key = 'aaaaaaabbbbcccc1'.encode('utf-8')
    mode = AES.MODE_ECB
    text = add_to_16(text)
    cryptos = AES.new(key, mode)

    cipher_text = cryptos.encrypt(text)
    return b2a_hex(cipher_text)

# 解密后，去掉补足的空格用strip() 去掉
def decrypt(text):
    key = 'aaaaaaabbbbcccc1'.encode('utf-8')
    mode = AES.MODE_ECB
    cryptor = AES.new(key, mode)
    plain_text = cryptor.decrypt(a2b_hex(text))
    return bytes.decode(plain_text).rstrip('\0')

if __name__ == '__main__':
    e = encrypt("15316005023")  # 加密
    d = decrypt(e)  # 解密
    print("加密:", e)
    print("解密:", d)