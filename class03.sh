#!/bin/bash

# 03/26/2024

# Script: Ops 301 Challenge 03
# Author: Steve Cherewaty
# Purpose: Adjust permissions

# Show the file permissions for the test file
ls -al

#Ask user for the name of the file to change permissions
echo "Please enter directory name intended for permission changes:"
read input_testdir

echo $input_testdir

# Change permisssions
chmod 777 $input_testdir

# See changes
ls -al

#end