# Using Nodefault

Make sure to import nodefault at the start of your os-faults script.
`import nodefault as nf`

## nf.nodeop(cloud_config, instruction)

Cloud_config is the configuration of your setup (same as os-faults).

Example: nf.nodeop(cloud_config,'(op) (node)')

(node) can be the fqdn of a single node, a list of multiple nodes or simply 'all'.

(op) is one of the following operations:
*reboot
*reset (cold restart of the machine)
*shutdown
*freeze (freezes the cpu activity)

## Examples

nf.nodeop(cloud_config,'shutdown compute1.node.net')

nf.nodeop(cloud_config,'reboot all')
