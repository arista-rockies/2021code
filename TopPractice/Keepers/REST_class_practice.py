import requests
import json
from pprint import pprint
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)  # This will disable invalid cert warnings


cvp_user = 'cvadmin'
cvp_pass = 'cvadmin'
cvp_host = '192.168.10.100'

auth_data = json.dumps({'userId': cvp_user, 'password': cvp_pass})
auth_url = auth_url = "https://%s/cvpservice/login/authenticate.do" % cvp_host
auth_response = requests.post(auth_url, data=auth_data, verify=False)
assert auth_response.ok
cookies = auth_response.cookies


class Cvpapi():
    def __init__(self, user=cvp_user, passwd=cvp_pass, cvp=cvp_host):
        self.user = user
        self.passwd = passwd
        self.cvp_host = cvp
        self.url = 'https://{}/cvpservice'.format(cvp_host)

    def add_switch(self, *ip):
        url_cvp = self.url + '/inventory/devices'
        switch_ip = json.dumps({'hosts': ip})
        rest_task = requests.post(url_cvp, cookies=cookies, data=switch_ip, verify=False)
        print(url_cvp)
        return rest_task

    def delete_switch(self, *sn):
        url_cvp = self.url + '/inventory/devices'
        switch_sn = json.dumps({'data': sn})
        rest_task = requests.delete(url_cvp, cookies=cookies, data=switch_sn, verify=False)
        print(url_cvp)
        return rest_task



        # device_ip: '10.10.10.2',
        # parent_name: 'MyContainer',
        # parent_key: 'container-id-1234'
remove = Cvpapi().delete_switch("JPE19181498", 'E5867DBAEA932A8CAFF35F0418BE712C')


# url_device_inventory = "https://192.168.10.100/cvpservice/inventory/devices?provisioned=false"
# task_params = {'startIndex': '0', 'endIndex': '0'}
# # adddev = Cvpapi().add_switch('192.168.10.1', '192.168.10.47')
# #requests.get(task_url, cookies=cookies, params=task_params, verify=False)
# result = requests.get(url_device_inventory, cookies=cookies, params=task_params, verify=False)
# print(result.json())
