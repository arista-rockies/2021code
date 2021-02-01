from jsonrpclib import Server
from pprint import pprint as pp
import signal
import yaml
import os
import time

def yload(data):
    safeload = yaml.load(data, Loader=yaml.FullLoader)
    return safeload



class TimeExceededError(object):
    pass


def timeout(signum, frame):
    raise TimeoutError


signal.signal(signal.SIGALRM, timeout)

numdevs = int(input("Yo sancheeze, how many ips you want me to get after? "))
baseip = '192.168.10.30'

def url(x):
    myurl = f'http://admin:admin@{x}/command-api'
    return myurl

def runcmds(z):
    base = int(baseip.split('.')[-1])
    x = 0
    while x < z:
        print(x, z)
        ip = '.'.join(baseip.split('.')[:-1]) + '.' + str(x + base)
        testnum = int(ip.split('.')[-1])
        print(testnum)
        if testnum < 50 or testnum > 60:
            try:

                signal.alarm(3)
                print(ip)
                switch = Server(url(ip))
                result = switch.runCmds(1, ['configure', 'write memory'])
                print(result)

            except:
                print('Not Arista!')
        x += 1





runcmds(numdevs)





