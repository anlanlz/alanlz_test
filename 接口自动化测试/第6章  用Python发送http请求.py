# 本章主要讲了http请求的Python+requests框架，
# 列举了使用框架发送各种请求方法，
# 还介绍了用fiddler抓Python的包，
# 还有用python下载文件的示例。

# print(response.text)            #文本形式打印网页源码
# print(response.status_code)             #打印状态码
# print(response.url)         #打印url
# print(response.headers)     #打印信息头
# print(response.cookies)     #打印cookie

# pro = {"http":"http://127.0.0.1:8888","https":"http://127.0.0.1:8888"}      #fiddler抓Python请求，将fiddler作为代理服务器

#verify=False       #关闭证书验证(ssl)，访问https

# 各种请求
# get，post，put,head,delete,options

# s = requests.session()        #会话维持

import pprint
import json
import requests

#会话维持
s = requests.session()
pro = {"http":"http://127.0.0.1:8888","https":"http://127.0.0.1:8888"}
loginUrl = "https://user.360kad.com/Login/AjaxLoginV2"
loginBody = {"userName":"16634412766","pass":"xiaokeailz508"}
loginResponse = s.post(loginUrl,data=loginBody,verify=False,proxies=pro)
print(loginResponse.text, '\n', loginResponse.headers, '\n', loginResponse.url,'\n',loginResponse.status_code)








