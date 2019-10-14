import os
import json
import psutil



def execute(command, key, username, ip, fqdn, op, node):
    
    if 'all' in command:
        try:
            print("%s %s" % (op, ip))
            parameter = ''
            if not op == 'slowoom':
                if op == 'oom':
                    parameter = command.split()[3]
                
                os.system("ssh -i %s %s@%s nohup 'bash -s' < ops/%s.sh &" % (key, username, ip, op, parameter)) 
            else:
                parameter = command.split()[5]
                if not isinstance(parameter, int):
                    parameter = 1
                for i in range(parameter):
                    os.system("ssh -i %s %s@%s nohup 'bash -s' < ops/%s.sh &" % (key, username, ip, op)) 


        except:
            print()

    elif fqdn in command or ip in command:
        try:
            print("%s %s" % (op, ip))
            parameter = ''

            if op == 'oom':
                parameter = command.split()[3]

            os.system("ssh -i %s %s@%s nohup 'bash -s' < ops/%s.sh %s &" % (key, username, ip, op, parameter)) 
            

        except:
            print()