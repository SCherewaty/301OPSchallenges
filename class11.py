#!/usr/bin/env python 3

# 04/08/2024

# Script: Ops 301 Challenge 07
# Author: Steve Cherewaty
# Purpose: Psutil

import psutil


# CPU time
print(f"CPU Time: {psutil.cpu_times()}\n")
# Time executing Kernel mode
print(f"CPU Consumption: {psutil.cpu_percent()}\n")
# Idle time
print(f"CPU Consumption: {psutil.times_idle()}\n")
# Time spent by priority process executing in user mode
print(f"CPU Consumption: {psutil.times.nice()}\n")
#  Time spent waiting for I/O  
print(f"CPU Consumption: {psutil.ctimes.iowait()}\n")
# Time spent servicing hardware interupts
print(f"CPU Consumption: {psutil.times.irq()}\n")
# Time spent servicing software interupts
print(f"CPU Consumption: {psutil.times.softirq()}\n")
# Time spent by other OS's in VM's
print(f"CPU Consumption: {psutil.times.steal()}\n")
# Time spent running virtual CPU for guests
print(f"CPU Consumption: {psutil.times.guest()}\n")



