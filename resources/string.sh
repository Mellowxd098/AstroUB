#!/bin/bash
clear
echo "
    _        _             
   / \   ___| |_ _ __ ___  
  / _ \ / __| __| '__/ _ \ 
 / ___ \ __ \ |_| | | (_) |
/_/   \_\___/\__|_|  \___/

"

sleep 5
apt-get update
apt-get upgrade -y
pkg upgrade -y
pkg install python wget -y
wget https://raw.githubusercontent.com/AstroUB/AstroUB/resources/AstroSetup.py
pip install telethon
python AstroSetup.py