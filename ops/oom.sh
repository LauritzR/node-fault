#!/bin/bash

mem=$(awk '/MemFree/{printf "%d\n", $2*1;}' < /proc/meminfo)
sudo stress --vm-bytes $mem*$1k --vm-keep -m 1 # -t 20
