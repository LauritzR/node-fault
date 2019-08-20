import os
import json
import psutil


def drop(command, ip, username, key):
    for e in command.split():
        perc = ' '
        if '%' in e:
            perc = e.strip()
        
    os.system("ssh -i %s %s@%s sudo tc qdisc change dev eno1 root netem loss %s>&-" % (key, username, ip, perc))
            

def slow(command, ip, fqdn, username, key):
    if ip in command or fqdn in command:
        print(ip)
        for e in command.split():
            perc = ' '
            if 'ms' in e:
                delay = e
        try:
            #print('slow with %s delay' % (delay))
            os.system("ssh -i %s %s@%s sudo tc qdisc add dev eno1 root netem delay %s>&-" % (key, username, ip, delay))
        except:
            print() 
    elif 'all' in command:
        for e in command.split():
            perc = ' '
            if 'ms' in e:
                delay = e
        try:
            print('slow with %s delay' % (delay))
            os.system("ssh -i %s %s@%s sudo tc qdisc add dev eno1 root netem delay %s>&-" % (key, username, ip, delay))
        except:
            print() 
