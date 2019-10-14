import os
import json
import psutil


def loop(command, key, username, ip, fqdn, op, node):
    loop = parameter = command.split()[4]
    com = ""

    print("%s %s %s" % (op, ip, loop))

    for i in range(int(loop)):
        com += "ops/oom.sh &"

    
    os.system("ssh -i %s %s@%s nohup 'bash -s' < %s" % (key, username, ip, com)) 
