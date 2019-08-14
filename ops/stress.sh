#!/bin/bash

sudo stress --cpu  $(nproc) --timeout 20 & disown