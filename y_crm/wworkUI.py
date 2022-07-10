# encoding=utf-8
# selenium2.0 = webdriver
import requests,re,pytesseract,selenium

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from PIL import Image
s = Service("D://pythonproject//pythonProjectyin//driver//chromedriver.exe")
driver = webdriver.Chrome(service=s)
s = requests.session()
#设置Fiddler代理
pro = {"http":"http://127.0.0.1:8888","https":"https://127.0.0.1:8888"}
# mydriver = webdriver.Chrome(executable_path="D://pythonproject//pythonProjectyin//driver//chromedriver.exe")
#最大化网址
mydriver.maximize_window()
#get输入网址
gdUrl = mydriver.get("http://gd.crm.yintech.net/#/login")
#等待
sleep(3)




#获取验证码截图
screenshot = mydriver.get_screenshot_as_base64()
url= "http://www.bhshare.cn/imgcode/"
query_string = {"access_token":"a15d4dec1"}
Headers = {"Content-type":"application/json"}
# screenshot_urlencoded = urllib.parse.quote(screenshot_base64)
payload = "image"
rew = s.post(url= url,params=query_string,headers=Headers,data=payload)
print(rew)


usernameGD = mydriver.find_element(By.CLASS_NAME,"el-input__inner").send_keys("zhao.li2")
passwordGD = mydriver.find_element(By.XPATH,"/html/body/div[2]/section/div[1]/div/div/div/form/div[2]/div/div/input").send_keys("Lz123456")
element = mydriver.find_element(By.XPATH,"/html/body/div[2]/section/div[1]/div/div/div/form/div[3]/div/div/div[2]/img")
element.screenshot("code.png")
code = input("请输入验证码")
mydriver.find_element(By.XPATH,"/html/body/div[2]/section/div[1]/div/div/div/form/div[3]/div/div/div[1]/div/input").send_keys(code)
mydriver.find_element(By.XPATH,"/html/body/div[2]/section/div[1]/div/div/div/form/div[5]/div/button/span").click()


loginbutton = mydriver.find_element(By.XPATH,"/html/body/div[2]/section/div[1]/div/div/div/form/div[4]/div/button/span")
loginbutton.click()

tasksaveurl = "http://gd.crm.yintech.net/api/v1/GD/WEB/TD/wechat/task/save"
bodytasksave = {"sendNumJs":[{"uid":"1688856783279700","cusNum":16,"groupNum":0}],
                "sendStatus":0,"msg":[{"type":"1","txt":{"content":"（测试消息）\n上海发布《关于做好全市新一轮核酸筛查工作的通告》\n","timestamp":1648430858}}],
                "sendTime":1648431530,"taskId":"202203280927490000","taskName":"正常模式账号群发",
                "cuids":{"1688856783279700":["1688858095332978","1688856783279700","1688854557264709","7881300162101852","1688850267387885","1688852647387034","7881300503168704","1688855922302141","7881301056907918","7881302962972143","7881299718926361","7881300716123984","1688856654252562","1688857667251193","1688852647387869","1688857247275400"]}}
respsave = s.post(tasksaveWW,data=bodytasksave)
print(respsave.text)
#
# orderurl="https://cart.360kad.com/Order/CreateOrder"
# bodydataorder={'AddressId':'11805275221','PayType':'1','InvoiceType':'0','InvoiceTitle':'','InvoiceCustomerType':'1',
#                'InvoiceDutyParagraph':'','IsInvoice':'0','CartType':'0','SendTimeType':'0','Remark':'','CouponCode':'',
#                'PointsAmt':'0','SendType':'1'}
# resp2=s.post(orderurl,data=bodydataorder)
# print(resp2.text)
#
# groupsendUrl = mydriver.get("http://gd.crm.yintech.net/#/createGroupTask")
# sleep(2)
#
# zhuti = mydriver.find_element(By.ID,"step_1").send_keys("测试")
# customer = mydriver.find_element(By.XPATH,"/html/body/div[2]/div/div[2]/section/div[2]/div/section/section/main/div/div[3]/div/div[2]/div/div[2]/div/div[1]/div/input")
# account = mydriver.find_element(By.XPATH,"/html/body/div[3]/div[1]/div[1]/ul/li[3]/span")