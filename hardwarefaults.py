import os
import json
import psutil



def execute(command, key, username, ip, fqdn, op, node):
    
    if 'all' in command:
        try:
            print("%s %s" % (op, ip))
            os.system("ssh -i %s %s@%s nohup 'bash -s' < ops/%s.sh &" % (key, username, ip, op)) 

        except:
            print()

    elif fqdn in command or ip in command:
        try:
            print("%s %s" % (op, ip))
            os.system("ssh -i %s %s@%s nohup 'bash -s' < ops/%s.sh &" % (key, username, ip, op)) 
            

        except:
            print()