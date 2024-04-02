#!/usr/bin/env python 3

# 04/02/2024

# Script: Ops 301 Challenge 07
# Author: Steve Cherewaty
# Purpose: Python script using os.walk

# Define a function 
def my_first_function():
    
    print("This is inside the function.")
    
# Define a second function
def function_with_parameters(name):
    print(f"Your name is: {name}")
    
# call function
my_first_function()
#function_with_parameters("Steve")

# Ask user for their name
username = input("Enter your username:")
function_with_parameters(username)

