# node-fault

An extension for os-faults to enable operations on nodes for physical machines instead of VMs.

In order to use it add the `nodefault.py` file together with the `ops` directory to the directory containing your os-faults python script.
Then simply `import nodefault` in your script and your are ready to go.

With nodefault you can

* reset (cold restart)
* reboot
* freeze (stop cpu)
* shutdown

your nodes.
