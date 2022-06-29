#! /bin/bash

read -p "Enter your username: " username
read -p "Enter your name: " name
read -p "Enter your position: " position
read -p "Enter your password: " password

echo "username : $username"
echo "Name : $name"
echo "Position : $position"
echo "temporary password: $password"
sudo useradd -m -c "this guy is $position"  $username &&sudo  passwd $username

if [[ $(echo $?) -eq 0 ]]
then
     echo "Your user account has been successfully created. Please do not forget to change your password"
fi


#!/bin/bash
#
# This script creates a new user on the local system.
# You will be prompted to enter the username (login), the person name, and a password.
# The username, password, and host for the account will be displayed.

# Make sure the script is being executed with superuser privileges.


# Get the username (login).


# Get the real name (contents for the description field).


# Get the password.


# Create the account.


# Check to see if the useradd command succeeded.
# We don't want to tell the user that an account was created when it hasn't been.


# Set the password.


# Check to see if the passwd command succeeded.


# Force password change on first login.


# Display the username, password, and the host where the user was created.
