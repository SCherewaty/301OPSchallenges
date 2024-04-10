#!/usr/bin/env python 3

# 04/08/2024

# Script: Ops 301 Challenge 07
# Author: Steve Cherewaty
# Purpose: Psutil

import psutil


# CPU time
print(f"CPU Time: {psutil.cpu_times()}\n")
# Time executing Kernel mode
print(f"Kernel Execution: {psutil.cpu_percent()}\n")
# Idle time
print(f"Idle Time: {psutil.times_idle()}\n")
# Time spent by priority process executing in user mode
print(f"User Mode By Priority: {psutil.times.nice()}\n")
#  Time spent waiting for I/O  
print(f"Time Waiting On I/O: {psutil.ctimes.iowait()}\n")
# Time spent servicing hardware interupts
print(f"Hardware Servicing Time: {psutil.times.irq()}\n")
# Time spent servicing software interupts
print(f"Software Servicing Time: {psutil.times.softirq()}\n")
# Time spent by other OS's in VM's
print(f"OS In Virtual Environment: {psutil.times.steal()}\n")
# Time spent running virtual CPU for guests
print(f"Guest CPU Running Under Linux Kernel: {psutil.times.guest()}\n")




