# Setting up the inject node

## Update dependencies
- `sudo apt-get update`
- `sudo apt-get upgrade`

## Install pip
- `sudo apt install python3-pip`
- `pip3 install pkgconfig`

## Install ansible
- `sudo apt install ansible`

## Install os-faults
- `pip3 install os-faults`

## Move needed files
- ` scp -r hardwarefaults.py inject.py networkfaults.py nodefault.py slowoom.py recover.py config.json ops user@node:.`
