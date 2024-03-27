#!/bin/bash

# 03/26/2024

# Script: Ops 301 Challenge 02
# Purpose: Append date and time

# Current date 
month= date +%m
day= date +%d
year= date +%y
# Current time
hour= date +%H
minutes= date +%M
seconds= date +%S

# Copy the syslog file to the current directory
cp /var/log/syslog ./ 

echo "Current Date: $day-$month-$year" >> syslog
echo "Current Time: $hour:$minutes:$seconds" >> syslog 


