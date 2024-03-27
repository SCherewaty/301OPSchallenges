#!/bin/bash

# 03/26/2024

# Script: Ops 301 Challenge 02
# Author: Steve Cherewaty
# Purpose: Change file permissions

# Show the file permissions for the test file
ls -al

#Ask user for the name of the file to change permissions
echo "Please enter file name intended for permissions changes:"
read input_filename

echo $input_filename

# Change permisssions
chmod 755 $input_filename

# See changes
ls -al

#end