#!/usr/bin/env python 3

# 04/02/2024

# Script: Ops 301 Challenge 07
# Author: Steve Cherewaty
# Purpose: Tuples and lists


# Assign a variable to a list of 10 string elements
parts_list = ["gears", "harnesses", "sheets", "sprockets", "tools", "glue", "wires", "transistor", "Pi", "lcd"]
print("These are your parts: " + str(parts_list))

#  Print the 4th item on the list
print("Element 4 only:")
print(parts_list[3])


# Print the 6th through the 10th item on the list
print("Elements 6-10 only:")
print(parts_list[:5])

# Add something 
parts_list[6] = "glue"
print(parts_list)











