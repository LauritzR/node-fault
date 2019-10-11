import os
import json
import psutil


def drop(command, ip, fqdn, username, key):
    perc = command.split()[2]  

    if 'from' in command:
        if ip in command or fqdn in command:
            source = command.split()[4]
            print('drop %s on %s' % (perc, fqdn))
            os.system("ssh -i %s %s@%s sudo iptables -A INPUT -s %s -m statistic --mode random --probability %s -j DROP" % (key, username, ip, source, perc))
    else:
        if ip in command or fqdn in command:
            print('drop %s on %s' % (perc, fqdn))
            os.system("ssh -i %s %s@%s sudo iptables -A INPUT -m statistic --mode random --probability %s -j DROP" % (key, username, ip, perc))
            #os.system("ssh -i %s %s@%s sudo iptables -D INPUT -m statistic --mode random --probability %s -j DROP" % (key, username, ip, perc)) #remove rule
            

def slow(command, ip, fqdn, username, key):
    delay = command.split()[2]
    if ip in command or fqdn in command:
        try:
            print('slow %s with %s delay' % (fqdn, delay))
            os.system("ssh -i %s %s@%s sudo tc qdisc add dev eno1 root netem delay %s" % (key, username, ip, delay))
        except:
            print
    elif 'all' in command:
        try:
            print('slow with %s delay' % (delay))
            os.system("ssh -i %s %s@%s sudo tc qdisc add dev eno1 root netem delay 100ms" % (key, username, ip, delay))
        except:
            print
