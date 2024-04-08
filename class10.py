#!/usr/bin/env python 3

# 04/05/2024

# Script: Ops 301 Challenge 07
# Author: Steve Cherewaty
# Purpose: Python File Handling

# Check file existence (I created the testfiles first)
import os
if os.path.exists("testfile1.txt"):
    print("It's real!")

# Open a file for reading
file = open("testfile1.txt", "r")

file.close()

# Try a file to write
#file = open("testfile2.txt", "w")

file.write("Hello Worldo")

file.close()












