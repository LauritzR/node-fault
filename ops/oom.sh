#!/bin/bash

mem=$(bc -l <<< $(awk '/MemFree/{printf "%d\n", $2;}' < /proc/meminfo)*$1)k
sudo stress -q --vm-bytes $mem --vm-keep -m 1 # -t 20
