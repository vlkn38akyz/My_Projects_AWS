#!/bin/bash

day=$(date)
hostname=$(hostname -s)
archive_file="$hostname-$day.tgz"


i=1


while [[ i=1 ]]
do 
tar -cvzf etc/$archive_file /etc
tar -cvzf boot/$archive_file /boot
tar -cvzf data1/$archive_file /home/ec2-user/data
sleep 60

done
