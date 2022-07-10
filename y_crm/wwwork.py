import requests

# 1、企业微信-多开
s = requests.session()
multiopenurl = "http://127.0.0.1:10560/func/multiopen"
multiopenbody = {"cmdline":"C:\\Program Files (x86)\\WXWork\\WXWork.exe","id":[""]}
multiopen = s.post(multiopenurl,data=multiopenbody)
print(open)

# 2、企业微信移除
softopturl = "http://127.0.0.1:10560/func/softopt"
softoptbody = {"cmdline":"C:\\Program Files (x86)\\WXWork\\WXWork.exe","id":[""]}
softopen = s.post(softopturl,data=softoptbody)
print(softopen)

# 3、企业微信移除

# 4、WeDK获取版本号
requ=requests.get("http://127.0.0.1:10560/func/softcheck?type=version")
print(requ.text)
