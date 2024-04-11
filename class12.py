#!/usr/bin/env python 3

# 04/09/2024

# Script: Ops 301 Challenge 07
# Author: Steve Cherewaty
# Purpose: Libraries

# Import libraries
import requests

# Define variables

# Ask the user for web address
address = input("Type the destination URL (format: google.com): \n ")

# Concatenate hhtps with user input
user_url = str('https://' + address)
print(user_url)

# Ask the user for the HTTP method they want to use
choice = input("Please select a method from the following list: \n get \n post \n put \n delete \n head \n patch \n options \n Type in your selection:")

# Conditional - checking what the user gave us
if choice == 'get':
    method = requests.get
elif choice == 'post':
    method = requests.post
elif choice == 'put':
    method = requests.put
elif choice == 'delete':
    method = requests.delete
elif choice == 'head':
    method = requests.head
elif choice == 'patch':
    method = requests.patch
elif choice == 'options':
    method = requests.options
else:
    print("Invalid Selection; just go with 'get'")
    method = requests.get
    
# Send the request using the method the user chose
response = method(user_url)
        
# Define functions
# Function that handles user output based on input
def run_command():
    confirm = input("Please confirm you want to run the following comand: \n \n requests." + choice + "('" + user_url +"') ----> \n Enter 'y' to confirm or 'n' to cancel.") 

    if confirm == 'y':
        print("\n The status code is: " + str(response.status_code))
        if response.status_code == 200:
            print("That\'s the code for a successful request.")
        elif response.status_code == 307:
            print("That\'s the code for a temporary redirect.")
        elif response.status_code == 400:
            print("That\'s the code for a bad request.")
        elif response.status_code == 403:
            print("403? - You don/'t have permission to access this...")
        elif response.status_code == 404:
            print("That\'s the code for site not found.")
        else: 
            print("Code not recognized.")
    else: 
        print("\nOkay we/'ll try to run it again.")
        
    print("Now..your header information:\n")
    print(response.headers)
    
            
# Call our function
run_command()


#TESTS
#print(response.text)
#print(response.headers)
#print(response.content)
#print(response.status_code)







