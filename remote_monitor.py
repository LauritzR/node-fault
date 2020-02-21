import json
import os
import time
import requests
import json_value_grabber as jvg
import sys




def get(ip, iteration):
    # ...request all possible netdata metrics...
    URL = "http://" + ip + ":19999/api/v1/allmetrics"
    parameter = {
        'format': "json",
        'help': "no",
        'types': "no",
        'timestamps': "no",
        'names': "yes",
        'oldunits': "no",
        'hideunits': "no",
        'data': "as-collected"
            }
    r = requests.get(url = URL, params=parameter)
    data = r.json()
    name = 'out'+str(iteration)+ '.json'

    # convert the results to the wanted format
    with open (name,'w') as out:
        json.dump(data, out, indent=4)
    name_edit = 'out'+str(iteration)+'_edit.json'
    jvg.grab('out'+str(iteration)+'.json', 'out'+str(iteration)+'_edit.json')
    
    # write them in the folder for the node they are from
    os.system('mv %s %s' % (name_edit, ip))


def monitor(timesteps_n, timesteps_length_sec, ip):

    # for the specified number of timesteps
    for i in range(timesteps_n):
        get(ip, i)
        time.sleep(timesteps_length_sec)

   



monitor(int(sys.argv[1]),int(sys.argv[2]), str(sys.argv[3]))