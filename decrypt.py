#!/usr/bin/env python3

import os
import sys
from cryptography.fernet import Fernet


files = []
for file in os.listdir():
    if file in ("encrypt.py", "thekey.key", "decrypt.py"):
        continue
    if os.path.isfile(file):
        files.append(file)

print("Files to decrypt:", files)


key_input = input("Enter full path to 'thekey.key' (or press Enter if it's in the same folder): ").strip()

# for slashes in windows
key_input = key_input.replace("\\", "/")

# for path simplification will accept the folder or the key path
if key_input == "":
    key_path = "thekey.key"
elif key_input.lower().endswith("thekey.key"):
    key_path = key_input  
else:
    key_path = os.path.join(key_input, "thekey.key")  

# verify
if not os.path.exists(key_path):
    print(f"❌ Error: '{key_path}' not found. Please check the path and try again.")
    sys.exit(1)

# key read
with open(key_path, "rb") as key_file:
    secretkey = key_file.read()


for file in files:
    try:
        with open(file, "rb") as thefile:
            contents = thefile.read()
        contents_decrypted = Fernet(secretkey).decrypt(contents)
        with open(file, "wb") as thefile:
            thefile.write(contents_decrypted)
        print(f"✅ Decrypted: {file}")
    except Exception as e:
        print(f"⚠️ Failed to decrypt {file}: {e}")
