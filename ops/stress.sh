#!/bin/bash

sudo stress --cpu  $(nproc) & disown