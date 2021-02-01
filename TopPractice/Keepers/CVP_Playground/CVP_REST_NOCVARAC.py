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

# print auth_response.json()

task_params = {'startIndex': '0', 'endIndex': '0'}
task_url = 'https://%s/cvpservice/inventory/devices?provisioned=false' % cvp_host
task_response = requests.get(task_url, cookies=cookies, params=task_params, verify=False)

pprint(task_response.json())


# newurl = 'https://%s/cvpservice/inventory/devices' % cvp_host
# datas = json.dumps({"hosts": ["192.168.10.1"]})
# newtask = requests.post(newurl, cookies=cookies, data=datas, verify=False)
# print(newtask)

device_url = 'https://%s/cvpservice/inventory/devices' % cvp_host
# del_datas = json.dumps({"data": ["JPE19181498"]})
# newtasks = requests.delete(device_url, cookies=cookies, data=del_datas, verify=False)
# print(newtasks)

def senddel(*macs, url=device_url):
    mac = json.dumps({'data': macs})
    send_url = requests.delete(url, cookies=cookies, data=mac, verify=False)
    return send_url

