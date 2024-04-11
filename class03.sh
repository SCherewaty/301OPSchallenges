#!/bin/bash

# 03/26/2024

# Script: Ops 301 Challenge 03
# Author: Steve Cherewaty
# Purpose: Adjust permissions

# Show the file permissions for the test file
ls -al

#Ask user for the a directory to change permissions name of the file to change permissions in the form of 3 digits
echo "Please enter directory name intended for permission changes: "
read input_testdir

#Ask user for the permissions - in the form of 3 digits
echo "Please provide the intended permissions (enter 3 digits): "
read input_perm

echo $input_testdir

# Change permisssions
chmod -R $input_testdir $input_testdir

# See changes 
ls -al $input_testdir

#end