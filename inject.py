import os_faults
import logging
import nodefault as nf
import time

cloud_config = {
        'cloud_management': {
            'driver': 'devstack',
            'args': {
                'address': 'pc734.emulab.net',
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
                    'connection_uri': 'qemu+ssh://stack@pc734.emulab.net/system?keyfile=.ssh/geni'
                }
            }
        ],

        'node_discover': {
            'driver': 'node_list',
            'args': [
                {   
                    'fqdn': 'pc734.emublab.net',
                    'ip': '155.98.36.34',
                    'libvirt_name': 'pc734',
                    'auth': {
                        'username': 'stack',
                        'private_key_file': '~/.ssh/geni'
                    }
                },
                {   
                    'fqdn': 'pc724.emublab.net',
                    'ip': '155.98.36.24',
                    'libvirt_name': 'pc724',
                    'auth': {
                        'username': 'stack',
                        'private_key_file': '~/.ssh/geni'
                    }
                },
                {
                    'fqdn': 'pc721.emublab.net',
                    'ip': '155.98.36.21',
                    'libvirt_name': 'pc721',
                    'auth': {
                        'username': 'stack',
                        'private_key_file': '~/.ssh/geni'
                    }
                }
            ]
        }
    }

#cloud_management = os_faults.connect(cloud_config)
#cloud_management.verify()
#nf.setup(cloud_config)

nf.nodeop(cloud_config,'reboot pc734.emublab.net')
nf.nodeop(cloud_config,'reset pc724.emublab.net')
nf.nodeop(cloud_config,'shutdown pc721.emublab.net')




#os_faults.human_api(cloud_management, 'poweroff pc734.emublab.net node')




