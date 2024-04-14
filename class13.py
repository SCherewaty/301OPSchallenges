#!/usr/bin/env python 3

# 04/10/2024

# Script: Ops 301 Challenge 07
# Author: Steve Cherewaty
# Purpose: Powershell AD automation

# Add a new user to the active directory
New-ADUser

# Include first name
-Name "Franz"
# Include Surname
-Surname "Ferdinand"
# Include title 
-Title "TPS Reporting Lead"
# Include Division
-Division "Globex USA"
# Include City
-City "Springfield"
# Include state
-State "OR"
# Include department
-Department "TPS"
# Include email
-EmailAddress "ferdi@globexpower.com"
