#!/bin/bash


# use -t to adjust timeout
sudo stress --vm-bytes $(awk '/MemFree/{printf "%d\n", $2 * 0.9;}' < /proc/meminfo)k --vm-keep -m 1 # -t 20