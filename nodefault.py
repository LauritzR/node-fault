import os
import json
import psutil

OPERATIONS = "freeze, oom, reboot, reset, shutdown, slowoom, stress"


def setup(config):
   for e in config['node_discover']['args']:
      print("Preparing %s" % (e['fqdn']))
      ip = e['ip']
      username = e['auth']['username']
      key = e['auth']['private_key_file']
      os.system("scp -r -i %s ops %s@%s:. >&- " % (key, username, ip)) 
      os.system("ssh -i %s %s@%s sudo apt-get install stress >&-" % (key,username,ip)) 


def nodeop(config, command):

   op = command.partition(' ')[0]

   if op not in OPERATIONS:
      print('Pleasespecify a valid operation.')

   for e in config['node_discover']['args']:
      ip = e['ip']   
      username = e['auth']['username']   
      key = e['auth']['private_key_file']

      
      if 'all' in command:
         try:
            print("%s %s" % (op, ip))
            os.system("ssh -i %s %s@%s 'bash -s' < ops/%s.sh >&-" % (key, username, ip, op)) 
         except:
            print()

      elif op == 'drop':
         if 'all' in command:
            for n in len(command.partition(' ')):
               if command.partition(' ')[n] == 'on':
                  on_ip = command.partition(' ')[n+1]
         os.system("ssh -i %s %s@%s tcpkill %s >&-" % (key, username, on_ip, on_ip))


      elif e['fqdn'] in command:
         try:
            print("%s %s" % (op, ip))
            os.system("ssh -i %s %s@%s 'bash -s' < ops/%s.sh >&-" % (key, username, ip, op)) 
         except:
            print()
            
   








