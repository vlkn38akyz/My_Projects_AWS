#!/bin/bash

# Check if we are root privilage or not




# Which files are we going to back up. Please make sure to exist /home/ec2-user/data file
backup_files="/usr"

# Where do we backup to. Please crete this file before execute this script
dest="/home/ec2-user/mnt/backup"

# Create archive filename based on time
day=$(date+%A)
hostname=$(hostname -s)
archive_file="$hostname-$day.tgz"

# Print start status message.
echo "Backing up $backup_files to $dest/$archive_file"
date
echo

# Backup the files using tar.
tar -czf $dest/archive_file $backup_files
# Print end status message.
echo 
echo "Backup finished"

# Long listing of files in $dest to check file sizes.
ls -lh $dest