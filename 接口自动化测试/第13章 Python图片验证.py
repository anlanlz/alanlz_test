import pytesseract,requests
from PIL import Image

s = requests.session()
#设置fiddler代理
# pro = {"http":"http://127.0.0.1:8888","https":"https://127.0.0.1:8888"}
#打开登录页面
loginUrl = "http://gd.crm.yintech.net/#/login"
# loginPageRes = s.get(loginUrl,verify=False,proxies=pro)
#获取页面中的token
# tokenPattern =

#获取图片验证码并存入本地
# imgUrl = "http://192.168.18.227:8585/user-center-server/api/v1/kaptcha?uuid=99fcf173-4139-465b-82de-260e9defcfbb "

#识别验证码
pytesseract.pytesseract.tesseract_cmd = 'C://Program Files (x86)/Tesseract-OCR/tesseract.exe'
gdImgNum = pytesseract.image_to_string(Image.open('E://1.png'))
print(gdImgNum)