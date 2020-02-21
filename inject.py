import os_faults
import logging
import nodefault as nf
import time
import json
import os
import monitor
import sys

with open('config.json') as file:
    cloud_config = json.load(file)

cloud_management = os_faults.connect(cloud_config)
cloud_management.verify()
nf.setup(cloud_config)

for n in cloud_config['node_discover']['args']:
   os.system("ssh -i ~/.ssh/geni stack@%s python recover.py & disown" % (n['ip']))

monitor.monitor(sys.argv[1],sys.argv[2])

time.sleep(5)

nf.nodeop(cloud_config, 'node oom 0.3 on all')