#!/bin/sh
echo "########################"
ifconfig
echo "########################"
id
echo "########################"
python podip.py
echo "########################"
wget -qO- http://172.30.183.243:8080

