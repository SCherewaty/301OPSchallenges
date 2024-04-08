#!/usr/bin/env python 3

# 04/02/2024

# Script: Ops 301 Challenge 07
# Author: Steve Cherewaty
# Purpose: Python Conditional Statements

laser_status = "Good"
condition = "clean"
internal_temp = "90"
external_temp = "80"
particulate_mass = "light"
tube_life = "40"

# If statement
if laser_status == "good":
    print("Laser ready to use!")
    
 # If else statement
if condition == "dirty": 
     print("The laser is dirty. Clean it dummy!")
else:
    print("The laser is clean. Get to work!")
    
# If-elif-else statement
if internal_temp <= 100:
    print("The tube is good to go.")
elif internal_temp > 100:
    print("The tube's gonna blow!.")
else:
    print("You'll prolly be okay...")
    
# Nested statements
if particulate_mass == "light":
    print("Optimal particulate mass.")
    if external_temp > 70:
        print("Gettin' warm in here...")
    elif external_temp <= 85 and external_temp > 45:
        print("It's cool enough to use the laser.")
    else:
        print("It's too hot now but it'll cool down later...hopefully.")
        
elif particulate_mass == "light":
    print("Particulate mass is optimal.")
else:
    print("I don't know, ask chat GPT what the particulate mass is.")
    

    
    
    