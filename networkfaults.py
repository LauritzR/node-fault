import os
import json
import psutil


def drop(command, ip, username, key):
    on = command.partition(' ')[1]

    for e in command.partition(' '):
        perc = ' '
        if '%' in e:
            perc = e
    
    os.system("ssh -i %s %s@%s tc qdisc change dev eno1 root netem loss %s>&-" % (key, username, ip, perc))
            

def slow(command, ip, username, key):
    on = command.partition(' ')[1]

    for e in command.partition(' '):
        perc = ' '
        if 'ms' in e:
            delay = e
    
    os.system("ssh -i %s %s@%s tc qdisc change dev eth0 root netem delay %s>&-" % (key, username, ip, delay))
            