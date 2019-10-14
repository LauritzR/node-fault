#!/bin/bash

procs=$(bc -l <<< $(nproc)*$1)

sudo stress -q --cpu  $procs