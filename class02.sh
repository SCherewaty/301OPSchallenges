#!/bin/bash

# 03/26/2024

# Script: Ops 301 Challenge 02
# Author: Steve Cherewaty
# Purpose: Append date and time


today=$(date +%m%d%y)

# Copy the syslog file to the current directory
cp /var/log/syslog ./syslog.$today





