import os
import json
import psutil


def drop(command, ip, fqdn, username, key):
    perc = command.split()[2]  
    if ip in command or fqdn in command:
        os.system("ssh -i %s %s@%s sudo iptables -A INPUT -m statistic --mode random --probability %s -j DROP" % (key, username, ip, perc))
            

def slow(command, ip, fqdn, username, key):
    if ip in command or fqdn in command:
      
        delay = command.split()[2]
        try:
            print('slow %s with %s delay' % (fqdn, delay))
            print(key)
            print(username)
            print(ip)
            os.system("ssh -i %s %s@%s sudo tc qdisc add dev eno1 root netem delay %s" % (key, username, ip, delay))
        except:
            print
    elif 'all' in command:
        for e in command.split():
            if 'ms' in e:
                delay = command.partition(' ')[2]
        try:
            print('slow with %s delay' % (delay))
            os.system("ssh -i %s %s@%s sudo tc qdisc add dev eno1 root netem delay 100ms" % (key, username, ip, delay))
        except:
            print
