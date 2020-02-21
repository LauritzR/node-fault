#!/usr/bin/env bash

iptables -P INPUT ACCEPT
tc qdisc del dev eth0 root