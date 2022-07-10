import os

import requests
import pytest


class Testclass(object):
    @pytest.mark.sikp(reason = "这是测试")
    def testcase_01(slef,tmpdir):
        s = requests.session()
        login_url = "http://gd.crm.yintech.net/api/v1/loginLdap"
        login_body = {"domainAccount": "weKldzx9SX9yActswRMYyw==", "password": "ivyyGn2hVnfPgKIGv3IlYA=="}
        login_response = s.post(login_url, data=login_body, verify=False)
        # pprint.pprint(login_response.json())
        # verify=False忽略证书
        assert "登陆成功" in login_response.text
    def testcase_02(slef, tmpdir):
        s = requests.session()
        login_url = "http://gd.crm.yintech.net/api/v1/loginLdap"
        login_body = {"domainAccount": "weKldzx9SX9yActswRMYyw==", "password": ""}
        login_response = s.post(login_url, data=login_body, verify=False)
        # pprint.pprint(login_response.json())
        # verify=False忽略证书
        assert "密码不能为空" in login_response.text
    def testcase_03(slef,tmpdir):
        s = requests.session()
        login_url = "http://gd.crm.yintech.net/api/v1/loginLdap"
        login_body = {"domainAccount": "", "password": "ivyyGn2hVnfPgKIGv3IlYA=="}
        login_response = s.post(login_url, data=login_body, verify=False)
        # pprint.pprint(login_response.json())
        # verify=False忽略证书
        assert "账号或密码不能为空" in login_response.text
    def testcase_04(slef,tmpdir):
        s = requests.session()
        login_url = "http://gd.crm.yintech.net/api/v1/loginLdap"
        login_body = {"domainAccount": "", "password": ""}
        login_response = s.post(login_url, data=login_body, verify=False)
        # pprint.pprint(login_response.json())
        # verify=False忽略证书
        assert "账号或密码不能为空" in login_response.text
if __name__ == '__main__':
    pytest.main(['-vs',  '--alluredir=./tmp'])
    os.system('allure generate ./tmp -o ./report --clean')