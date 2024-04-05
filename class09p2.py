#!/usr/bin/env python 3

# 04/02/2024

# Script: Ops 301 Challenge 07
# Author: Steve Cherewaty
# Purpose: Python Conditional Statements

#AND statements: BOTH things have to be true
#OR statements: Only one needs to be true

forecast = "sunny"
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
    
# Nested statements
if wind == "strong":
    print("It's windy outside.")
    if pollen_count > 70:
        
    elif pollen_count <= 70 and pollen_count > 30:
        print("It's windy with a moderate pollen count.")
    else:
        print("No worries, it's windy but with a low pollen count")
        
elif wind == "weak":
    print("The wind is weak today.")
else:
    print("Wind conditions are unknown")
           
# Complex logical conditions
if forecast == "rain" or wind == "strong":
    print("The weather sucks today, stay inside.")
elif temperature > 75 and humidity > 70:
    print("It's too hot and humid today.")
elif not forecast == 75 and temperature >= 50:
    print("It's too hot and humid today.")
else: 
    print("Weather conditions are unknown. ")
    
    
