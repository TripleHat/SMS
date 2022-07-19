#!/bin/bash

if [[ -e "$PATH/python" ]]
then
	echo -e "\033[9$(( RANDOM % 6 ))m"
else
	echo -e "\033[9$(( RANDOM % 6 ))m[!] Please Wait..."
	pkg install python -y > /dev/null
fi

python main.py
