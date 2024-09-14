# MacChanger-MACX
macx is a python script with which you can change your mac address. 

## Overview 
MACX is a Python script designed to change the MAC address of a network interface on Unix-based systems. It also verifies whether the MAC address has been changed successfully.

## Features 
Changing the MAC address of a specific network interface. - Verifying the new MAC address. - Providing clear feedback in case of success or failure. 

## Platforms 
This script is designed to run on the following Unix-based systems:
-Linux
-macOS
-Termux 

##Setup
Use: python macchanger.py -i <network interface> -m <new_mac_address> 

Explanation: -i, --interface : Network interface to change -m, --mac : New MAC address

Example: python macchanger.py -i eth0 -m 00:11:22:33:44:55



Operation on Windows systems is not guaranteed. ## Setup To use MAC Changer, you need Python 3 and the `colorama, sys, subprocess, re, optparse` modules. You can install the module with pip. 
Telegram: t.me/pizza_0day
