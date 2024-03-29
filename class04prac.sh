#!/bin/bash

# 03/28/2024

# Script: Ops 301 Challenge 04
# Author: Steve Cherewaty
# Purpose: Conditional statement practice

# echo $target
target=$RANDOM
let "target %= 100"
let "target += 1"


# create the loop
while true; do 
    echo "Guess a number between 1 and 100:"
    read guess
    echo $guess

# Is the guess correct?
    if [ $guess -eq $target ]; then 
    echo "You got it!"
    fi

# Is the guess too high or too low?
    if [ $guess -gt $target ]; then 
        echo "Too high...try again."
    else 
        echo "Too low...try again."
    fi

done