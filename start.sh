#!/bin/bash

if [ "$EUID" == 0 ]
  then echo "Please run Without Root"
  exit
fi

if [[ -e "$PATH/python3" ]]
then
	echo -e "\033[9$(( RANDOM % 6 ))m"
else
	echo -e "\033[9$(( RANDOM % 6 ))m[!] Please Wait..."
	apt install python -y > /dev/null
fi

python3 main.py
