# How to setup openstack

## Perform on all nodes

* `sudo su root`
* `useradd -s /bin/bash -d /opt/stack -m stack`
* `echo "stack ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers`
* `sudo su stack`
* `cd`
* `mkdir ~/.ssh; chmod 700 ~/.ssh`
* `echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC+7IY6mQI3tAojpeseSaSHTgN+HT8Xnhsus8FICbU6p5T2SRtEF2N4c5LV4/zV5Qvnd/VR/wHMdfWVuaMqAPlIDeuxztRvZUrkRbcwiD1M8xFE9iTfgHF9zcrDHRUQ71LSXErrYaJ9XYDL1UJifMrOdSPQi5HncgtNMmxjv9VUS8k+XV4TcMXoUKi5IF5QUQdaVuEmQYkj1Wk0UyKHjRnTC79T0LfXPbCFPUM4PLvO1DbGCmGz/85xfhBW8jhRt679+3dXPlvcgSEB17MWOC59mWTpLmXB16jbjpRNNzSTl/VcbZBUMtFgGV6mEWc8A814oigbuBLKAE9vVLPyZ5T9 LauritzRasbach@Lauritzs-MacBook-Pro.local" > ~/.ssh/authorized_keys`
* `git clone https://opendev.org/openstack/devstack`
* `cd devstack`

## Perform only on control node

* Get the machine's IP address
* `nano local.conf`
* \[[local|localrc]]
    HOST_IP=192.168.42.11\
    FIXED_RANGE=10.4.128.0/20\
    FLOATING_RANGE=155.98.36.128/25\
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
* \[[local|localrc]]
    HOST_IP=192.168.42.12 # change this per compute node\
    FIXED_RANGE=10.4.128.0/20\
    FLOATING_RANGE=155.98.36.128/25\
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
