import os
import json
import psutil

def setup(config):
   for e in config['node_discover']['args']:
      print("Preparing %s" % (e['fqdn']))
      ip = e['ip']
      username = e['auth']['username']
      key = e['auth']['private_key_file']
      os.system("scp -r -i %s ops %s@%s:. >&- " % (key, username, ip)) 
      os.system("ssh -i %s %s@%s sudo apt-get install stress >&-" % (key,username,ip)) 


def nodeop(config, command):
   if 'reboot' in command:
      op = 'reboot'
   elif 'shutdown' in command:
      op = 'shutdown'
   elif 'freeze' in command:
      op = 'freeze'
   elif 'reset' in command:
      op = 'reset'  
   elif 'oom' in command:
      op = 'oom'
   else:
      print('Please specify an operation.')

   for e in config['node_discover']['args']:
      ip = e['ip']   
      username = e['auth']['username']   
      key = e['auth']['private_key_file']

      
      if 'all' in command:
         try:
            print("%s %s" % (op, ip))
            os.system("ssh -i %s %s@%s 'bash -s' < ops/%s.sh" % (key, username, ip, op)) 
         except:
            print()

      elif e['fqdn'] in command:
         try:
            print("%s %s" % (op, ip))
            os.system("ssh -i %s %s@%s screen 'bash -s' < ops/%s.sh" % (key, username, ip, op)) 
            os.system(" ")
         except:
            print()
            
   






### Write scripts for shutdown, reboot, freeze (cpu)
### Upload scripts with setup
### when functions are called, execute on desired node
### write readme



