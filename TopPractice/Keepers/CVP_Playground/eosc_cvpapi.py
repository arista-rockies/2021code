from pprint import pprint
from cvprac.cvp_client import CvpClient
from cvprac.cvp_client_errors import CvpApiError
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)  # This will disable invalid cert warnings
# Instantiate Client and connect to CVP nodes
client = CvpClient()
client.connect(['192.168.10.100'], 'cvadmin', 'cvadmin')

# Define new configlet name and content
configlet_name = 'VLANS'
configlet_content = 'vlan 100\n   name DEMO\nend'

node = 'jpatterson-720'

# Check if we already have a configlet by this name
try:
    configlet = client.api.get_configlet_by_name(configlet_name)
except CvpApiError as err:
    if 'Entity does not exist' in err.msg:
        # Configlet doesn't exist let's create one
        result = client.api.add_configlet(configlet_name, configlet_content)
        pprint(result)
    else:
        raise
else:
    # Configlet does exist, let's update the content
    result = client.api.update_configlet(configlet_content, configlet['key'], configlet_name)
    pprint(result)

configlet_info = client.api.get_configlet_by_name(configlet_name)
pprint(configlet_info)

getconfiglets = client.api.get_configlets()
pprint(getconfiglets)
# Get our device
device_info = client.api.get_device_by_name(node)
pprint(device_info)

# Check if the configlet is already applied to this device
current_configlets = client.api.get_configlets_by_device_id(device_info['systemMacAddress'])
found = False
for applied_configlet in current_configlets:
    if applied_configlet['key'] == configlet_info['key']:
        found = True

# Apply configlet to our device if it is not already applied
if not found:
    response_data = client.api.apply_configlets_to_device('APP_NAME', device_info,
                                                          [configlet_info], create_task=True)
    pprint(response_data)
    # Execute task returned
    if 'taskIds' in response_data['data'] and response_data['data']['taskIds']:
        client.api.execute_task(response_data['data']['taskIds'][0])

test = 'test'