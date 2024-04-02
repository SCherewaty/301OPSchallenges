#!/usr/bin/env python 3

# 04/02/2024

# Script: Ops 301 Challenge 07
# Author: Steve Cherewaty
# Purpose: Python script using os.walk

# Define a function 
def make_a_sandwich(user_name):
    
    print(f"Hi {user_name}!")
    
    # prompt the user to enter sandwich ingredients
    bread = input("What type of bread?")
    cheese = input("What type of cheese?")
    meat = input("what type of meat?")
    veggies = input("what type of veggies?")
    condiments = input("what type of toppings?")
    
    # initialize a tuple with sandwich ingredients
    sandwich_ingredients = (bread, cheese, meat, veggies, condiments)
   # square brackets indicate a list
   # sandwich_ingredients = [bread, cheese, meat, veggies, condiments]
   
   print(f"\nThis is {user_name}'s favorite sandwich: ")
   
   # Unpack the tuple in a for loop and print each ingredient
    for ingredients in (sandwich_ingredients):
       print(ingredients)
    
       
       user = input("What is your name: ")
       make_a_sandwich(user)
       
    
    