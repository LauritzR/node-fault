import os
import json
import psutil

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

   op = command.partition(' ')[0]

   if op not in OPERATIONS:
      print('Pleasespecify a valid operation.')

   for e in config['node_discover']['args']:
      ip = e['ip']   
      username = e['auth']['username']   
      key = e['auth']['private_key_file']

   # drop on ... except ...

      ### Block for dropping packets
      if op == 'drop':
         get_on = False
         get_except = False
         excepted = ''

         for n in len(command.partition(' ')):
            if get_on:
               on = command.partition(' ')[n]
               get_on = False
            
            if get_except:
               excepted += ' '
               excepted += command.partition(' ')[n]

            if command.partition(' ')[n] == 'on':
               get_on = True
            if command.partition(' ')[n] == 'except':
               get_except = True

         ### execute on all nodes
         if 'all' in on:
            if excepted == '':
               os.system("ssh -i %s %s@%s tcpkill host %s >&-" % (key, username, ip, ip))
            else:
               op = "ssh -i %s %s@%s tcpkill %s"
               for j in excepted:
                  op += ' and not '
                  op += excepted.partition(' ')[j]

               op += '>&-'
               os.system("ssh -i %s %s@%s tcpkill host %s %s>&-" % (key, username, ip, on, op))

         ### execute on ly on selected
         elif ip in on:
            if excepted == '':
               os.system("ssh -i %s %s@%s tcpkill host %s >&-" % (key, username, ip, ip))
            else:
               op = "ssh -i %s %s@%s tcpkill %s"
               for j in excepted:
                  op += ' and not '
                  op += excepted.partition(' ')[j]

               op += '>&-'
               os.system("ssh -i %s %s@%s tcpkill host %s %s>&-" % (key, username, ip, on, op))


      elif 'all' in command:
         try:
            print("%s %s" % (op, ip))
            os.system("ssh -i %s %s@%s 'bash -s' < ops/%s.sh >&-" % (key, username, ip, op)) 
         except:
            print()

      

      elif e['fqdn'] in command:
         try:
            print("%s %s" % (op, ip))
            os.system("ssh -i %s %s@%s 'bash -s' < ops/%s.sh >&-" % (key, username, ip, op)) 
         except:
            print()
            
   








