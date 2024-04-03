#!/usr/bin/env python 3

# 04/02/2024

# Script: Ops 301 Challenge 07
# Author: Steve Cherewaty
# Purpose: Python script using os.walk

# impport libraries
import os

# function

# Use os walk from os library

# os walk in a function
def first_python_function(dir_name):
    for (root,dirs,files) in os.walk("/home/steve/" + dir_name)
    print("===root===")
    print(root)
    
    print("===dirs===")
    print(dirs)
    
    print("===dirs===")
    print(dirs)
    

    
user_input = input("Type the name of the directory")
    
first_python_function(user_input)
