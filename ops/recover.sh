#!/usr/bin/env bash

sudo iptables -P INPUT ACCEPT
sudo tc qdisc del dev eno1 root
sudo coldreboot