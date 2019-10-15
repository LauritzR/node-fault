import os
import json
import psutil
import slowoom as so



def execute(command, key, username, ip, fqdn, op, node):
    
    if 'all' in command:
        try:
            parameter = ''
            
            if op == 'oom' or op == 'stress':
                parameter = command.split()[2]
 
            print("%s %s %s" % (op, ip, parameter))
            os.system("ssh -i %s %s@%s nohup 'bash -s' < ops/%s.sh %s &" % (key, username, ip, op, parameter)) 
        except:
            print()

    elif fqdn in command or ip in command:
        try:
            parameter = ''
            
            # get the parameters needed for oom and stress (memory  and cpu utilization)
            if op == 'oom' or 'stress' in op:
                parameter = command.split()[2]
            loop = 1

            # if there is a speed parameter given and the operation is slowoom, set the speed
            if command.split()[4].isdigit() and op == 'slowoom':
                loop = command.split()[4]

            print("%s %s %s %s" % (op, ip, parameter, loop))

            # perform operation n times (higher speed = faster memory filling)
            for i in range(int(loop)):
                os.system("ssh -i %s %s@%s nohup 'bash -s' < ops/%s.sh %s &" % (key, username, ip, op, parameter)) 
        except:
            print()