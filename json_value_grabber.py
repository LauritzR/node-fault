import json
import os

dat = {}


def dig(name, block):
    for (k, v) in block.items():
        if isinstance(v,int) or isinstance(v,float):
                if name == "":
                    dat[k] = float(v)
                else:
                    dat[name + "_" + k] = float(v)
        elif isinstance(v, dict):
            if name == "":
                    dig(k, v)
            else:
                dig(name+"_"+k, v)
            
    return


# Function for grabbing integer and float values from a json file
def grab(inputf, outputf):
    f = open(inputf)
    data = json.load(f)
    f.close
    dig("", data)
    with open (outputf,'w') as out:
        json.dump(dat, out, indent=4)
    os.system("rm -r %s" % (inputf))

