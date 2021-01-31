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
device_url = 'https://%s/cvpservice/inventory/devices' % cvp_host
# print auth_response.json()

# task_params = {'startIndex': '0', 'endIndex': '0'}
# task_url = 'https://%s/cvpservice/inventory/devices?provisioned=false' % cvp_host
# task_response = requests.get(task_url, cookies=cookies, params=task_params, verify=False)
#
# pprint(task_response.json())

# def add_dev(*ip, url=device_url):
#     ip = json.dumps({"hosts": list(ip)})
#     task = requests.post(url, cookies=cookies, data=ip, verify=False)
#     return task
#
# add_dev('192.168.10.47', '192.168.10.1')

# ip = json.dumps({"hosts": ["192.168.10.47"]})
# task = requests.post(device_url, cookies=cookies, data=ip, verify=False)
# print(task)

# del_datas = json.dumps({"data": ["JPE19181498"]})
# newtasks = requests.delete(device_url, cookies=cookies, data=del_datas, verify=False)
# print(newtasks)

# def senddel(*macs, url=device_url):
#     mac = json.dumps({'data': macs})
#     task = requests.delete(url, cookies=cookies, data=mac, verify=False)
#     return task
# senddel("JPE19181498", "E5867DBAEA932A8CAFF35F0418BE712C")


def testunpack(*mylist):
    print(list(mylist))
    for i in mylist:
        print(i)

var1 = 'var1'
var2 = 'var2'

testunpack('192.168.10.47', '192.168.10.1')