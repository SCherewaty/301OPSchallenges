#!/bin/bash

# 03/29/2024

# Script: Ops 301 Challenge 05
# Author: Steve Cherewaty
# Purpose: Compress and clear contents of log files

# Copy a lof file
#cp /var/log/syslog ./syslog-test

# Create backup directory
# mkdir backups

#create variable that will call our backup directory
BACKUP_DIR="backups"
LOG_FILES= "syslog-test" "wtmp-test"

#generate a timestamp
TIMESTAMP=$(date +"%Y%m%d%H%M%S")
echo $TIMESTAMP

# Loop thru each log file and take all of these actions

for file in "${LOG_FILES[@]}"; do

    #print file size before compression
    FILE_SIZE=$(wc -c "$file" | awk {print $1})
    echo $FILE_SIZE

    # Compress the contents of the log files
    # /var/lo/syslog
    # /var/log/syslog

    FILE_NAME=$(basename "$file")
    zip -r "$BACKUP_DIR/$FILE_NAME-$TIMESTAMP.zip" "$file"

    # Generate a time stamp in the format - YYYMMDDHHMMSS

#clear the contents of the log file
cat /dev/null > "$file"

