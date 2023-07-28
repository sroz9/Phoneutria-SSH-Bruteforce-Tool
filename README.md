# Phoneutria SSH-An SSH Bruteforce-Tool

# What is Phoneutria?
Phoneutria SSH, or PSSH, is a Tool that uses an IP-Adress, an Username file and a Password file to try to log into 
a Computer using SSH.
Following things are to be rememberd when using PSSH:
              1. The legality of a brute force attack is dictated by intent. In other words, if you're attempting to maliciously access a user account or organization's network to cause harm through financial or other motivations, then it is illegal.
              2. For any Legal issues caused by PSSH, the user of the Software is responsable. Meaning that you should use this at your own risk!
              3. This Tool can be very time consuming, as Phoneutria will need to guess both the username and the password. This Tool also does NOT have a 100% chance of successing.
              4. Phoneutria can, depending on the users PC, cause lag.

# How to install and run?
To start the Software please make sure you have Python installed:

 https://www.python.org/downloads/
 
 In order for the Software to work correctly also make sure you have paramiko installed:
 
 pip install paramiko

 Once you have Python and paramiko installed, you should be able to run the script without any issues.
 Remember to save the script with a .py extension and execute it from the command line or terminal using:

 python Phoneutria.py
 
After Installed it will prompt you to enter the target IP address, username file path, and password file path as input for the script.

A username file (usernames.txt) will be provided with the Software.
You can also use other password/username files.

# LICENCE
The code is licensed under the MIT License.

