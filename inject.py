import os_faults
import logging
import nodefault as nf
import time

with open('config.json') as file:
    cloud_config = json.load(file)

cloud_management = os_faults.connect(cloud_config)
cloud_management.verify()
nf.setup(cloud_config)


# OOM   SLOWOOM     STRESS
nf.n# OOM   SLOWOOM     STRESS
nf.nodeop(cloud_config, 'node oom 0.9 on pc462.emulab.net')
nf.nodeop(cloud_config, 'node slowoom with speed 5 on pc531.emulab.net')
nf.nodeop(cloud_config, 'node stress 0.5 on pc453.emulab.net')


# SHUTDOWN  REBOOT  RESET
nf.nodeop(cloud_config, 'node shutdown on pc409.emulab.net')
nf.nodeop(cloud_config, 'node reboot on pc406.emulab.net')
nf.nodeop(cloud_config, 'node reset on pc461.emulab.net')


# SLOW  DROP
nf.nodeop(cloud_config, 'network slow 100ms on pc411.emulab.net')
nf.nodeop(cloud_config, 'network slow 300ms on pc451.emulab.net')
nf.nodeop(cloud_config, 'network slow 1000ms on pc452.emulab.net')

nf.nodeop(cloud_config, 'network drop 0.1 from pc440.emulab.net on pc416.emulab.net')
nf.nodeop(cloud_config, 'network drop 0.2 on pc440.emulab.net')
nf.nodeop(cloud_config, 'network drop 0.5 on pc410.emulab.net')
nf.nodeop(cloud_config, 'network drop 1 on pc413.emulab.net')


# KILL  TERMINATE   START
os_faults.human_api(cloud_management, 'kill nova-compute service on pc470.emulab.net node')
os_faults.human_api(cloud_management, 'terminate nova-compute service on pc404.emulab.net node')
time.sleep(20)
os_faults.human_api(cloud_management, 'start nova-compute service on pc470.emulab.net node')


