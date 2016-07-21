#!/bin/bash

printf "Enter new password: "
stty -echo
read pass < /dev/tty
printf "\nEnter begin: "
read pass2 < /dev/tty
printf "\n"
stty echo
