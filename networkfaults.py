import os
import json
import psutil


def drop(command, ip, username, key):
    on = command.partition(' ')[1]
    for e in command.partition(' '):
        perc = ' '
        if '%' in e:
            perc = e
    os.system("ssh -i %s %s@%s sudo tc qdisc change dev eno1 root netem loss %s>&-" % (key, username, ip, perc))
            

def slow(command, ip, fqdn, username, key):
    if ip in command or fqdn in command:
        print(ip)
        on = command.partition(' ')[1]
        for e in command.partition(' '):
            perc = ' '
            if 'ms' in e:
                delay = e
        try:
            #print('slow with %s delay' % (delay))
            os.system("ssh -i %s %s@%s sudo tc qdisc change dev eth0 root netem delay %s>&-" % (key, username, ip, delay))
        except:
            print() 
    elif 'all' in command:
        for e in command.partition(' '):
            perc = ' '
            if 'ms' in e:
                delay = e
        try:
            #print('slow with %s delay' % (delay))
            os.system("ssh -i %s %s@%s sudo tc qdisc change dev eth0 root netem delay %s>&-" % (key, username, ip, delay))
        except:
            print() 
