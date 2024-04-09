#!/usr/bin/env python 3

# 04/02/2024

# Script: Ops 301 Challenge 07
# Author: Steve Cherewaty
# Purpose: Python script using os.walk

# import libraries
import os

# Ask the user for a file path
user_input = input("type in the directory name from origin folder: ")

# os walk in a function
def python_function(dir_name):
    for (root,dirs,files) in os.walk("/home/stevamous/" + dir_name):
        # print root
        print("===root===")
        print(root)
        # print dirs
        print("===dirs===")
        print(dirs)
        # print files
        print("===files===")
        print(files)
        

# Call the function and pass the variable 
python_function(user_input)             

