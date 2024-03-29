#!/bin/bash

# 03/28/2024

# Script: Ops 301 Challenge 04
# Author: Steve Cherewaty
# Purpose: Creating menus

# create the user menu

echo "Hello World!"

if [ "`ping -c 1 127.0.0.1`" ]
then 
    echo 1
else
    echo 0
fi

echo "Network Adapter:"


