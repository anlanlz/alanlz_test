# -*- coding:utf-8 -*-

import codecs
import json
import pprint
import requests
import allure
import pytest
import os


@allure.feature("登陆")
@allure.feature("客户")
@allure.feature("人事")

# if __name__ == '__main__':
#     pytest.main(['-vs','crm_gd.py','--alluredir=./tmp'])
#     os.system('allure generate ./tmp -o ./report --clean')
    # os.system('allure open -h 127.0.0.1 -p 8883 ./report')


# 提取login中的token
#     lg_token = login_response.json().get('token')
#     print(lg_token)

# @allure.feature("登陆")
# def testcase_01():
#
#     addintentcus_Url = "http://gd.crm.yintech.net/api/v1/GD/WEB/TJ/myIntentCustomer/toAddIntentCus"
#     addintentcus_Body = {"custInfo.cusName":"李01","custInfo.cusGender":"1","custInfo.cusAge":"22","contact":"15203030203","naAreaNum":"0086","busTypId":"2","busChiTypId":"16"}
#     addintentcus_Headers = {"token":lg_token}
#     addintentcus_resp = s.post(addintentcus_Url,data=json.dumps(addintentcus_Body),headers=addintentcus_Headers,verify=False)
#     pprint.pprint(addintentcus_resp.json())
    # json.dumps()序列化




# 会话维持
# s = requests.session()

# 添加GD-TJ意向客户


# 新建群组
# saveG_url = "http://gd.crm.yintech.net/api/v1/GD/WEB/TD/wechat/groupSend/save"
# saveG_body = {"gids":{"1688856783279700":["10853067290686092"]},"labelIds":{"1688856783279700":["14073752957702562"]},"remarks":[],"sgName":"python新建群组","unLabelIds":{},"unRemarks":[]}
# saveG_headers = {"token":lg_token}
# saveG_response = s.post(saveG_url,data=json.dumps(saveG_body),headers=saveG_headers,verify=False)
# pprint.pprint(saveG_response.json())
# json.dumps()序列化

# # 发送消息
# def parse_page(a):
#     print(a.url)
#     with codecs.open('send_response.json',mode="w",encoding = "utf-8") as f:
#         # f.write(str(a.json()))
#         pprint.pprint(a.json())
# 和codecs模块结合使用，将结果\u6210\u529f这种格式转换成中文

# send_url = "http://127.0.0.1:10560/chat/multiple/send"
# send_body = {"space":"300-600","taskname":"新建群组","account":[{"type":1,"from":"1688856783279700","to":["1688858095332978","1688856783279700"]}],"filter":[],"message":[{"type":"1","txt":{"content":"测试消息","timestamp":1648435902}}],"timing":None}
# send_headers = {"token":lg_token}
# send_response = s.post(send_url,data=json.dumps(send_body),headers=send_headers,verify=False)
# pprint.pprint(send_response.json())
# print(send_response.json())

# 发送历史


