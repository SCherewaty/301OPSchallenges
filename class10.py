#!/usr/bin/env python 3

# 04/05/2024

# Script: Ops 301 Challenge 07
# Author: Steve Cherewaty
# Purpose: Python File Handling

# Check file existence (I created the testfiles first)
import os
if os.path.exists("testfile1.txt"):
    print("It's real!")

# Create new txt file
new_file = open("testfile2.txt", "w")
new_file.write("Here's the new test file.")
new_file.close()

# More practice

file = open("testfile2.txt", "w")
file.write("Hello Worldo")
file.close()

# Append 3 lines
new_file = open("testfile2.txt", "a")
new_file.close("/n")
new_file.write("Here's the 1 appended test file.")
new_file.write("Here's the 2 appended test file.")
new_file.write("Here's the 3 appended test file.")
new_file.close()

# Print one line at a time
read_file = open("Testfile1.txt", "r")

for line in read_file:
    print(line)

# Print the first line
print(read_file.readline())

# delete testfile
os.remove("testfile2.txt")
# rename
# os.remove("testfile2.txt")








