#! /bin/bash

day=$(date)
#day1=$(date)
hostname=$(hostname -s)
archive_file="$hostname-$day.tgz"
echo $archive_file | tr " " "."
sleep 60
echo $archive_file | tr " " "."
sleep 60 
echo $archive_file | tr " " "."
sleep 60
echo $archive_file | tr " " "."
echo $day
#$day1

