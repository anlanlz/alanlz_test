# encoding=utf-8

# selenium2.0 = webdriver
import selenium
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
mydriver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")

# executable_path="C:\\chromedriver.exe"
GDurl = mydriver.get("http://gd.crm.yintech.net/#/login")
sleep(2)
# id 定位器
# class 定位器
usernameGD = mydriver.find_element(By.CLASS_NAME,"el-input__inner").send_keys("zhao.li2")
passwordGD = mydriver.find_element(By.XPATH,"/html/body/div[2]/section/div[1]/div/div/div/form/div[2]/div/div/input").send_keys("Lz123456")
# passwordGD = mydriver.find_element(By.CLASS_NAME,"el-input__inner").send_keys("Lz123456")
loginbutton = mydriver.find_element(By.XPATH,"/html/body/div[2]/section/div[1]/div/div/div/form/div[4]/div/button/span")
loginbutton.click()
# XPTH 定位器
# mydriver.find_element(By.XPATH,"/html/body/div[2]/section/div[1]/div/div/div/form/div[1]/div/div/input").send_keys("zhao.li2")
# passwordGD = mydriver.find_element(By.XPATH,"/html/body/div[2]/section/div[1]/div/div/div/form/div[2]/div/div/input").send_keys("Lz123456",Keys.ENTER)
