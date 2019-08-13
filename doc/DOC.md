# My own os-faults documentation

## Kill

### Kill service on all nodes

os_faults.human_api(cloud_management, 'kill (service) service')

### Kill service on one node

os_faults.human_api(cloud_management, 'kill (service) service on (fqdn) node')

## Terminate

### Terminate service on all nodes

os_faults.human_api(cloud_management, 'terminate (service) service')

### Terminate service on one node

os_faults.human_api(cloud_management, 'terminate (service) service on (fqdn) node')

## Start

### Start service on all nodes

os_faults.human_api(cloud_management, 'start (service) service')

### Start service on one node

os_faults.human_api(cloud_management, 'start (service) service on (node) node')

## Restart

### Restart service on all nodes

os_faults.human_api(cloud_management, 'restart (service) service')

### Restart service on one node

os_faults.human_api(cloud_management, 'restart (service) service on (node) node')

## Reboot

### Reboot all nodes

os_faults.human_api(cloud_management, 'reboot all nodes')
nf.nodeop(cloud_config,'reboot all')

### Reboot one node

os_faults.human_api(cloud_management, 'reboot (node) node')
nf.nodeop(cloud_config,'reboot (node)')
//also works with multiple nodes

## Using Nodefault

### nf.nodeop(cloud_config, instruction)

Cloud_config is the configuration of your setup (same as os-faults).

Example: nf.nodeop(cloud_config,'(op) (node)')

(node) can be the fqdn of a single node, a list of multiple nodes or simply 'all'.

(op) is one of the following operations:
*reboot
*reset (cold restart of the machine)
*shutdown
*freeze (freezes the cpu activity)
