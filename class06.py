#!/usr/bin/env python3

# 04/01/2024

# Script: Ops 301 Challenge 06
# Author: Steve Cherewaty
# Purpose: Python script that executes in bash

# SImple print to the screen
print ("Hello World!")

# import a library / modules
import os
list = os.system("ls")
user = os.system("whoami")

# Executing command but redirecting output to a txt file
os.system("ls > list.txt")
os.system("whoami > user.txt")

# For loop
for file in ["list.txt", "user.txt"]:
    with open(file, "r") as content:
      
      output = content.read()
   
      
      #print out the contents using f-strings
    print(f"command output: {output}")
    print ("command output:" + output)
    
    
    
    

