from jsonrpclib import Server
from pprint import pprint as pp
import time
import signal
import yaml
import os


def yload(data):
    safeload = yaml.load(data, Loader=yaml.FullLoader)
    return safeload

class TimeExceededError(object):
    pass


def timeout(signum, frame):
    raise TimeExceededError


signal.signal(signal.SIGALRM, timeout)

numdevs = int(input("How many contiguous IPs ? "))
baseip = '192.168.10.64'

def url(x):
    myurl = f'http://admin:admin@{x}/command-api'
    return myurl

def runcmds(z):
    base = int(baseip.split('.')[-1])
    print(base)
    x = 0
    while x < z:
        try:
            signal.alarm(5)
            ip = '.'.join(baseip.split('.')[:-1]) + '.' + str(x + base)
            print(ip)
            switch = Server(url(ip))
            hostname = (switch.runCmds(1, ['show hostname'])[0]['hostname'])
            print(hostname)
            savecfg = os.system('sshpass -p "admin" scp admin@{}:/mnt/flash/startup-config /Users/jpatterson/Documents/#Arista/aristalab/rockiesevpn/vxlan-vxlan_l3_site-to-site/vxlan-vxlan-dci_{}.cfg'.format(ip, hostname))
            print('config saved!')
            print('*' * 20)
        except:
            print('Not Arista!')
        x += 1



runcmds(numdevs)





