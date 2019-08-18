#!/bin/bash

# not done yet
yes | tr \\n x | head -c $((1024*1024*1024)) | pv -L $((1024*1024*10)) | grep n & disown & kill -s 2 pid
