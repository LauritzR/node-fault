# How to setup openstack

## Perform on all nodes

* `sudo su root`
* `useradd -s /bin/bash -d /opt/stack -m stack`
* `echo "stack ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers`
* `sudo su stack`
* `cd`
* `mkdir ~/.ssh; chmod 700 ~/.ssh`
* `echo "ssh-rsa ...key..." > ~/.ssh/authorized_keys`
* `git clone https://opendev.org/openstack/devstack`
* `cd devstack`

## Perform only on control node

* Get the machine's IP address
* `nano local.conf`
* \[[local|localrc]]\
    HOST_IP=192.168.42.11\
    LOGFILE=/opt/stack/logs/stack.sh.log\
    ADMIN_PASSWORD=labstack\
    DATABASE_PASSWORD=supersecret\
    RABBIT_PASSWORD=supersecret\
    SERVICE_PASSWORD=supersecret\
    enable_plugin os-faults https://opendev.org/performa/os-faults master
* `nano local.sh`
* for i in \`seq 2 10`; do /opt/stack/nova/bin/nova-manage fixed reserve 10.4.128.$i; done
* `./stack.sh`

## Perform only on compute nodes

* wait until the control node is finished
* `nano local.conf`
* \[[local|localrc]]\
    HOST_IP=192.168.42.12 # change this per compute node\
    LOGFILE=/opt/stack/logs/stack.sh.log\
    ADMIN_PASSWORD=labstack\
    DATABASE_PASSWORD=supersecret\
    RABBIT_PASSWORD=supersecret\
    SERVICE_PASSWORD=supersecret\
    DATABASE_TYPE=mysql\
    SERVICE_HOST=192.168.42.11 # enter control nodes IP here\
    MYSQL_HOST=\$SERVICE_HOST\
    RABBIT_HOST=\$SERVICE_HOST\
    GLANCE_HOSTPORT=\$SERVICE_HOST:9292\
    ENABLED_SERVICES=n-cpu,q-agt,n-api-meta,c-vol,placement-client\
    NOVA_VNC_ENABLED=True\
    NOVNCPROXY_URL="http://\$SERVICE_HOST:6080/vnc_lite.html"\
    VNCSERVER_LISTEN=\$HOST_IP\
    VNCSERVER_PROXYCLIENT_ADDRESS=$VNCSERVER_LISTEN\
    enable_plugin os-faults https://opendev.org/performa/os-faults master
* `./stack.sh`

## Finalize

* Perform `./tools/discover_hosts.sh` on control node

## Validate

* on control node
* `. openrc admin admin`
* `openstack compute service list`
* check if all nodes show up
