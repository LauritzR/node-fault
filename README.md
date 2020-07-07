# node-fault

An extension for os-faults to enable operations on nodes for physical machines instead of VMs.

In order to use it add the `nodefault.py` file together with the `ops` directory to the directory containing your os-faults python script.
Then simply `import nodefault` in your script and your are ready to go.

With nodefault you can

* reset (cold restart)
* reboot
* freeze (stop cpu)
* shutdown
* oom (fill memory, 90%) 
* slowoom (slowly fill memory) 
* stress (stress cpus)
* stressdisk (specify number of workers performing read/write operations; can be used to either stress IO or fill storage)
* drop packets (make exceptions for traffic between specific nodes)
* slow connection (specify packet size for forced traffic)
* delay (specify delay time)

your nodes.
