#!/bin/bash


yes | tr \\n x | head -c $((1024*1024*1024)) | pv -L $((1024*1024*100)) | grep n