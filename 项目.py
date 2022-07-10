import requests
import re
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.66 Safari/537.36 Edg/103.0.1264.44',
    'Cookie': 'SF_cookie_1=37059734'
}
jsons =[]
url ="http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2018/index.html"

resource1 = requests.get(url=url,headers=headers).content.decode('gbk')
surl_list = re.findall("<td><a href='(.*?)'>",resource1)
sname_list = re.findall("html'>(.*?)<br/>",resource1)
for i in range(0, len(sname_list)):
    sshujv = {}   #每次加载新数据都会重新创建一个字典 为空
    surl = "http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2018/"+surl_list[i]
    sname = sname_list[i]
    sshujv['surl'] =surl
    sshujv['sname']=sname
    sshujv['value']=[]
    # jsons.append(sshujv)
    cresource = requests.get("http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2018/"+surl_list[i]).content.decode('gbk')
    cname_list = re.findall("html'>(.*?)</a>",cresource)
    # print(cresource)
    curl_list= re.findall("<a href='(.*?)'>",cresource)
    # print(curl_list)
    print("开始获取"+sname+"数据")
    for cname in range(0,len(curl_list)):
        cshujv={}
        if(cname%2==0):
            print("开始获取" + cname_list[cname+1] + "城市数据")
            cshujv['cbianhao']=cname_list[cname]
            cshujv['cname']=cname_list[cname+1]
            cshujv['curl']='http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2018/'+curl_list[cname]
            curl= 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2018/'+curl_list[cname]
            qresource =requests.get(url=curl).content.decode("gbk")
            qname_list =re.findall("html'>(.*?)</a></td>",qresource)
            qurl_list =re.findall("<a href='(.*?)'>",qresource)
            cshujv['value']=[]
            for qname in range(0,len(qname_list)):
                qshujv ={}
                if (qname % 2 == 0):
                    print("开始获取" + qname_list[qname + 1] +"数据"+"区") # 区
                    qshujv['qbianhao'] = qname_list[qname]
                    qshujv['qname'] = qname_list[qname + 1]
                    httr=""
                    for shuliang in range(0,len(curl)-9):
                        httr = httr+curl[shuliang]
                    qshujv['qurl']=httr+qurl_list[qname]
                    jresource = requests.get(httr+qurl_list[qname]).content.decode("gbk")
                    jname_list = re.findall("html'>(.*?)</a></td>", jresource)
                    jurl_list = re.findall("<a href='(.*?)'>", jresource)
                    qshujv['value']=[]
                    for jname in range(0, len(jname_list)):
                        jshujv = {}
                        if (jname % 2 == 0):
                            jshujv['jbianhao'] = jname_list[jname]
                            jshujv['jname'] = jname_list[jname + 1]
                            httree=httr + qurl_list[qname]
                            jhttr = ""
                            print(jshujv)
                            for urlen in range(0, len(httree) - 11):
                                jhttr += httree[urlen]
                            jhttr=jhttr+jurl_list[jname]
                            print(jhttr)
                            lresource = requests.get(jhttr).content.decode("gbk")
                            lname_list = re.findall("<td>(.*?)</td>", lresource)
                            jshujv['value'] = []
                            for lname in range(0, len(lname_list)-1):
                                lshujv = {}
                                if (lname_list[lname]!="名称" and lname%3==0):
                                    lshujv['jname'] = lname_list[lname]
                                    jshujv['value'].append(lshujv)
                        if(jshujv != {}):
                            qshujv['value'].append(jshujv)
                    if (qshujv != {}):
                        qshujv['value'].append(jshujv)
                if(qshujv!={}):
                    print("开始获取" + qname_list[qname + 1] + "数据获取成功")
                    cshujv['value'].append(qshujv)
            if(cshujv!={}):
                sshujv['value'].append(cshujv)
                print(sshujv)
    jsons.append(sshujv)
    print(sname+"数据获取成功\n\n\n")
print(jsons)
with open(r"C:/Users/qiuxiansheng/Desktop/项目/收货地址.txt",mode="a+",encoding="utf-8") as f:
    strqqt = str(jsons)
    f.write(strqqt)