import os
import json
import psutil



def execute(command, key, username, ip, fqdn, op, node):
    
    if 'all' in command:
        try:
            parameter = ''
            
            if op == 'oom' or op == 'stress':
                parameter = command.split()[2]
            loop = command.split()[4]

            print("%s %s %s" % (op, ip, parameter))

            if not isinstance(parameter, int):
                loop = 1
            for i in range(loop):
                os.system("ssh -i %s %s@%s nohup 'bash -s' < ops/%s.sh %s &" % (key, username, ip, op, parameter)) 
        except:
            print()

    elif fqdn in command or ip in command:
        try:
            print("%s %s" % (op, ip))
            parameter = ''
            
            if op == 'oom':
                parameter = command.split()[2]
            loop = command.split()[4]
            if not isinstance(parameter, int):
                loop = 1
            for i in range(loop):
                os.system("ssh -i %s %s@%s nohup 'bash -s' < ops/%s.sh %s &" % (key, username, ip, op, parameter)) 
        except:
            print()