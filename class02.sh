#!/bin/bash

# Script: Ops 301 Challenge 02
# Purpose: Append date and time

# Run date command from within our script
year= date +%Y

month= date +%M

echo $month

day= date +%d

hour= date +%H
minutes= date +%M
seconds= date +%S

#putting it all together
echo "Current Date: $day-$month-$year"

# How to append
echo "Original file before append:"
cat testfile.txt


