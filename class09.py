#!/usr/bin/env python 3

# 04/02/2024

# Script: Ops 301 Challenge 07
# Author: Steve Cherewaty
# Purpose: Tuples and lists

forecast = "rain"
sky = "cloudy"
temperature = 75
wind = "strong"
pollen_count = 80
humidity = 60

# If statement
if forecast == "rain":
    print("It is raining! Don't forget your rain jacket! ")
    
 # If else statement
if sky == "cloudy": 
     print("The sky os cloudy.")
else:
    print("The sky is clear.")
    
# If-elif-else statement
if temperature < 40:
    print("It's cold outside.")
elif temperature > 75:
    print("It's warm outside.")
else:
    print("The temperature is average.")
    
    
    