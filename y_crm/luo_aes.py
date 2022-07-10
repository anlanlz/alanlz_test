from tkinter import *
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex
from tkinter import ttk

root = Tk()
root.title('罗成涛学Python')
root.geometry('380x300+720+450')
root.resizable(width=True, height=True)



"""
aes加密算法
ECB模式
"""
def add_to_16(text):
    if len(text.encode('utf-8'))%16:
        add = 16 - len(text.encode('utf-8')) % 16
    else:
        add = 0
    text = text + ("\0"*add)
    return text.encode('utf-8')
Label(root,text="请输入要加密的字符串：").place(anchor="nw",x=0,y=0)
Label(root,text="请选择/输入秘钥（长度为16位）：").place(anchor="nw",x=0,y=50)
text_input = Entry(root,highlightcolor="red",highlightthickness=1,width=25)
text_input.place(anchor="nw",x=0,y=25)
select_widow=ttk.Combobox(root, font=("Arial",12),width=30)  #state="readonly"限制文本框是可选的
select_widow.place(anchor="nw",x=0,y=75)
select_widow["value"] = ("aaaaaaabbbbcccc1", "aaaaaaabbbbcccc1", "aaaaaaabbbbcccc1")


text1 = Text(root,width=25,height=8)
text1.place(anchor="nw",x=0,y=130)
def encrypt():
    text = text_input.get()
    key_input = select_widow.get()
    key = key_input.encode('utf-8')
    mode = AES.MODE_ECB
    text = add_to_16(text)
    cryptos = AES.new(key, mode)
    cipher_text = cryptos.encrypt(text)
    aes_secrt= b2a_hex(cipher_text).decode()
    text1.insert(END,aes_secrt)
b1 = Button(root,text="加密",width=6,height=1,command=encrypt)
b1.place(anchor="nw",x=0,y=100)



def decrypto():
    text11 = text1.get("1.0",'end-1c')
    key_input = select_widow.get()
    key = key_input.encode('utf-8')
    mode = AES.MODE_ECB
    cryptor = AES.new(key,mode)
    plain_text = cryptor.decrypt(a2b_hex(text11))
    ase_unsecrt = bytes.decode(plain_text).rstrip('\0')
    text2.insert(END, ase_unsecrt)

text2 = Text(root,width=25,height=8)
text2.place(anchor="nw",x=190,y=130)
b2 = Button(root,text="解密",width=6,height=1,command=decrypto)
b2.place(anchor="nw",x=190,y=100)
root.mainloop()