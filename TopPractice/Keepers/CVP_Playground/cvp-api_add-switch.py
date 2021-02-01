from cvprac.cvp_client import CvpClient
from cvp_py import cvp
import requests
import json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)  # This will disable invalid cert warnings

CVP_HOST = "192.168.0.5"
CVP_USER = "arista"
CVP_PWD = "arista"

# To remove warnings


clnt = CvpClient()
clnt.connect(['192.168.10.100'], 'cvadmin', 'cvadmin')
# result = clnt.get('/cvpInfo/getCvpInfo.do')
# print(result)

get_container = clnt.api.get_containers()
print(get_container)
# add_container = clnt.api.add_container('slcdc', 'Tenant', 'root')
# getdevs = clnt.get('/inventory/devices')
# print(getdevs)

movedev = clnt.api.add_device_to_inventory('192.168.10.1', 'slcdc', 'container_f5301252-9a51-42ac-81de-7813e34624c0')

# clnt.api.delete_device('fc:bd:67:0f:52:79')

# 'parent_name': 'slcdc', 'parent_key': 'container_f5301252-9a51-42ac-81de-7813e34624c0'})

