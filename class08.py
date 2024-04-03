#!/usr/bin/env python 3

# 04/02/2024

# Script: Ops 301 Challenge 07
# Author: Steve Cherewaty
# Purpose: Tuples and lists

# Create a tuple
thistuple = ("apple", "banana", "cherry", "Orange", "kiwi", "melon", "bread")
print("This is the tuple: " + str(thistuple))

# Create a list
grocery_list = ["apple", "banana", "cherry", "Orange", "kiwi", "melon", "bread"]
print("This is the list: " + str(thistuple))

# Print the first item in the list
# print("This is the first item in the list: " + grocery_list[0])

# print("This is the last item in the list: " + grocery_list[2])
# OR
# print("This is the last item in the list: " + grocery_list[-1])

# print a slice (range) of the list
# print 3rd to the 5th item
# print(grocery_list[2:5])

# Print from beginning of the list to a specific number
print(grocery_list[:4])

# Add an item to the list
grocery_list.append("steak")
print(grocery_list)

grocery_list.insert(1, "butter")
print(grocery_list)

grocery_list.remove("butter")
print(grocery_list)

# Print a slice of items with a step value
print(grocery_list[1:8:2])








