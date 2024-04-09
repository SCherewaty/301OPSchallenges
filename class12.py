#!/usr/bin/env python 3

# 04/09/2024

# Script: Ops 301 Challenge 07
# Author: Steve Cherewaty
# Purpose: Libraries

# Import libraries PART 1
# Import requests
# Import libraries PART 2
from requests import get

# Do a get request using the requests library and assign a variable
response = requests.get('https://api.github.com')

# PART 2 Do a get request using the requests library and assign a variable
response = get('https://api.github.com')

# print(response.text)
# print(response.headers)
# print(response.content)
print(response.status_code)

#new 





