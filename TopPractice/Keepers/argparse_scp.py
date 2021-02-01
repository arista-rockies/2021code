import argparse
import signal
import os

class TimeExceededError(object):
    pass


def timeout(signum, frame):
    raise TimeExceededError


signal.signal(signal.SIGALRM, timeout)


parser = argparse.ArgumentParser(description="SCP files from GNS3 bastion host \n"
                                             "###arg_values = parser.parse_args(['-u', 'admin', '-p', 'admin', '-i', '192.168.10.1', '-r', '1', '-s', '/mnt/flash/vEOS-lab-4.24.2.3F.swi', '-d', '/mnt/flash/'])###")


parser.add_argument('-u', '--username', action='store', dest='username', help='username for switches', default='admin')
parser.add_argument('-p', '--password', action='store', dest='password', help='password for switches', default='admin')
parser.add_argument('-i', '--ip', action='store', dest='base_ip', help='base IP address for range of switches', nargs=1, required=True)
parser.add_argument('-r', '--range', action='store', dest='number_of_switches', type=int, help='number of switches in the range', nargs=1, required=True)
parser.add_argument('-s', '--source', action='store', dest='source_file', help='Source path and file to SCP', required=True)
parser.add_argument('-d', '--destination', action='store', dest='dest_directory', help='Destination path-directory to SCP file to', default='/mnt/flash/')

arg_values = parser.parse_args(['-u', 'admin', '-p', 'admin', '-i', '192.168.10.1', '-r', '1', '-s', '/Users/jpatterson/Downloads/vEOS-lab-4.24.2.3F.swi'])

print(arg_values.username[0])

def scp_to_devs(z):
    base = int(arg_values.base_ip[0].split('.')[-1])
    print(base)
    x = 0
    while x < z:
        try:
            # signal.alarm(5)
            ip = '.'.join(arg_values.base_ip[0].split('.')[:-1]) + '.' + str(x + base)
            print('Starting to SCP to ' + ip)
            print('sshpass -p "{}" scp {} {}@{}:/mnt/flash/'.format(arg_values.password,
                                                                                   arg_values.source_file,
                                                                                   arg_values.username,
                                                                                   ip,
                                                                                   arg_values.dest_directory))

        except:
            print('Error - device failed to connect!')
        x += 1

scp_to_devs(arg_values.number_of_switches[0])