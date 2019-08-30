import os
import json
import psutil
import networkfaults as nw
import hardwarefaults as hw

OPERATIONS = "freeze, oom, reboot, reset, shutdown, slowoom, stress, drop"


def setup(config):
   for e in config['node_discover']['args']:
      print("Preparing %s" % (e['fqdn']))
      ip = e['ip']
      username = e['auth']['username']
      key = e['auth']['private_key_file']
      os.system("scp -r -i %s ops %s@%s:. >&- " % (key, username, ip)) 
      os.system("ssh -i %s %s@%s sudo apt-get install stress >&-" % (key,username,ip)) 


def nodeop(config, command):

   op = command.partition(' ')[1]

   if op not in OPERATIONS:
      print('Please specify a valid operation.')

   for e in config['node_discover']['args']:
      ip = e['ip']   
      username = e['auth']['username']   
      key = e['auth']['private_key_file']
      fqdn = e['fqdn']

      if 'network' in command:
         if 'drop' in command:
            nw.drop(command,ip,username,key)
         elif 'slow' in command:
            nw.slow(command,ip, fqdn, username,key)

      if 'node' in command:
         hw.execute(command, key, username, ip, fqdn,  op, e)
   








