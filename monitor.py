import json
import os
import time
import requests
import json_value_grabber as jvg
import sys


# setup function, uploads scripts etc...
def setup():
    with open('config.json') as file:
        cloud_config = json.load(file)

    for e in cloud_config['node_discover']['args']:
        ip = e['ip']
        print("Setting up %s" % (ip))
        os.system('scp -i ~/.ssh/geni remote_monitor.py stack@%s:.' % (ip))
        os.system('scp -i ~/.ssh/geni json_value_grabber.py stack@%s:.' % (ip))
        os.system('scp -i ~/.ssh/geni mkdir %s stack@%s:.' % (ip, ip))

    print("Setup complete!")


# actual monitoring function, monitors status and saves it on the nodes
def monitor(timesteps_n, timesteps_length_sec):
    with open('config.json') as file:
        cloud_config = json.load(file)

    command = ""
    for e in cloud_config['node_discover']['args']:
        ip = e['ip']
        command += ' ssh -i ~/.ssh/geni stack@%s python remote_monitor.py %s %s %s &' % (ip, timesteps_n, timesteps_length_sec, ip)
        #os.system('ssh -i ~/.ssh/geni stack@%s python remote_monitor.py %s %s %s' % (ip, timesteps_n, timesteps_length_sec, ip))
    os.system(command)

# function for downloading observations to the machine
def get_obs():
    with open('config.json') as file:
        cloud_config = json.load(file)

    for e in cloud_config['node_discover']['args']:
        ip = e['ip']
        os.system('scp -r -i ~/.ssh/geni stack@%s:%s ~/Desktop/Monitoring/' % (ip, ip))


#setup()
#monitor(int(sys.argv[1]),int(sys.argv[2]))
get_obs()
