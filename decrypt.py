#! /usr/bin/env python3

import os
import sys
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
        if file == "encrypt.py" or file == "thekey.key" or file == "decrypt.py":
                continue
        if os.path.isfile(file):
	        files.append(file)
	
print(files)

if not os.path.exists("thekey.key"):
    print("❌ Error: 'thekey.key' not found. Please ensure the key is in the same folder as this script.")
    sys.exit(1)
    
with open("thekey.key","rb") as key:
        secretkey = key.read()

for file in files:
        with open(file, "rb") as thefile:
                contents = thefile.read()
        contents_decrytped = Fernet(secretkey).decrypt(contents)
        with open(file, "wb") as thefile:
                thefile.write(contents_decrytped)
