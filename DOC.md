# Using Nodefault

Make sure to import nodefault at the start of your os-faults script.
`import nodefault as nf`

Additionally you have to run `nf.setup(config)` (with config being your os-faults configuration) in order to setup the nodes for fault injection.

## nf.nodeop(cloud_config, instruction)

Cloud_config is the configuration of your setup (same as os-faults).

Example: nf.nodeop(cloud_config,'(op) (node)')

(node) can be the fqdn of a single node, a list of multiple nodes or simply 'all'.

(op) has the following structure:
The first part is the instruction type, either 'node ' or 'network'.
The second part is one of the following instructions for 'node':
* reboot
* reset (cold restart of the machine)
* shutdown
* freeze (freezes the cpu activity)

or for 'network':
* drop (needs parameter for drop percentage, 0.01 = 1%)
* slow (needs parameter for slow down in ms)

At the end of each command is the name/ip of the node the command should be run on.
'Node' operations support the 'all' parameter for commands which should be executed on all nodes.

## Examples

nf.nodeop(cloud_config,'shutdown compute1.node.net')

nf.nodeop(cloud_config,'reboot all')
