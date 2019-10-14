import os_faults
import logging
import nodefault as nf
import time


cloud_config = {
        'cloud_management': {
            'driver': 'devstack',
            'args': {
                'address': 'pc470.emulab.net',
               	'auth':{
		 	'username': 'stack',
                	'private_key_file': '~/.ssh/geni'
	        }    
	    }
        },

        'power_managements': [
            {
                'driver': 'libvirt',
                'args': {
                    'connection_uri': 'qemu+ssh://stack@pc470.emulab.net/system?keyfile=.ssh/geni'
                }
            }
        ],

        'node_discover': {
            'driver': 'node_list',
            'args': [
                {   
                    'fqdn': 'pc470.emulab.net',
                    'ip': '155.98.38.70',
                    'libvirt_name': 'pc470',
                    'auth': {
                        'username': 'stack',
                        'private_key_file': '~/.ssh/geni'
                    }
                },
                {   
                    'fqdn': 'pc462.emulab.net',
                    'ip': '155.98.38.62',
                    'libvirt_name': 'pc462',
                    'auth': {
                        'username': 'stack',
                        'private_key_file': '~/.ssh/geni'
                    }
                },
                {
                    'fqdn': 'pc531.emulab.net',
                    'ip': '155.98.38.131',
                    'libvirt_name': 'pc531',
                    'auth': {
                        'username': 'stack',
                        'private_key_file': '~/.ssh/geni'
                    }
                },
                {   
                    'fqdn': 'pc409.emulab.net',
                    'ip': '155.98.38.9',
                    'libvirt_name': 'pc409',
                    'auth': {
                        'username': 'stack',
                        'private_key_file': '~/.ssh/geni'
                    }
                },
                {   
                    'fqdn': 'pc406.emulab.net',
                    'ip': '155.98.38.6',
                    'libvirt_name': 'pc406',
                    'auth': {
                        'username': 'stack',
                        'private_key_file': '~/.ssh/geni'
                    }
                },
                {   
                    'fqdn': 'pc461.emulab.net',
                    'ip': '155.98.38.61',
                    'libvirt_name': 'pc461',
                    'auth': {
                        'username': 'stack',
                        'private_key_file': '~/.ssh/geni'
                    }
                },
                {   
                    'fqdn': 'pc453.emulab.net',
                    'ip': '155.98.38.53',
                    'libvirt_name': 'pc453',
                    'auth': {
                        'username': 'stack',
                        'private_key_file': '~/.ssh/geni'
                    }
                },
                {   
                    'fqdn': 'pc411.emulab.net',
                    'ip': '155.98.38.11',
                    'libvirt_name': 'pc411',
                    'auth': {
                        'username': 'stack',
                        'private_key_file': '~/.ssh/geni'
                    }
                },
                {   
                    'fqdn': 'pc451.emulab.net',
                    'ip': '155.98.38.51',
                    'libvirt_name': 'pc451',
                    'auth': {
                        'username': 'stack',
                        'private_key_file': '~/.ssh/geni'
                    }
                },
                {   
                    'fqdn': 'pc452.emulab.net',
                    'ip': '155.98.38.52',
                    'libvirt_name': 'pc452',
                    'auth': {
                        'username': 'stack',
                        'private_key_file': '~/.ssh/geni'
                    }
                },
                {   
                    'fqdn': 'pc404.emulab.net',
                    'ip': '155.98.38.4',
                    'libvirt_name': 'pc404',
                    'auth': {
                        'username': 'stack',
                        'private_key_file': '~/.ssh/geni'
                    }
                },
                {   
                    'fqdn': 'pc416.emulab.net',
                    'ip': '155.98.38.16',
                    'libvirt_name': 'pc416',
                    'auth': {
                        'username': 'stack',
                        'private_key_file': '~/.ssh/geni'
                    }
                },
                {   
                    'fqdn': 'pc440.emulab.net',
                    'ip': '155.98.38.40',
                    'libvirt_name': 'pc440',
                    'auth': {
                        'username': 'stack',
                        'private_key_file': '~/.ssh/geni'
                    }
                },
                {   
                    'fqdn': 'pc410.emulab.net',
                    'ip': '155.98.38.10',
                    'libvirt_name': 'pc410',
                    'auth': {
                        'username': 'stack',
                        'private_key_file': '~/.ssh/geni'
                    }
                },
                {   
                    'fqdn': 'pc413.emulab.net',
                    'ip': '155.98.38.13',
                    'libvirt_name': 'pc413',
                    'auth': {
                        'username': 'stack',
                        'private_key_file': '~/.ssh/geni'
                    }
                },
            ]
        }
    }

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


