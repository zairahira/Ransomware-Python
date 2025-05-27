# Create a ransomware in Python using Fernet cryptography

This Python application encrypts all the files in its current folder. A key is generated using the [Fernet](https://cryptography.io/en/latest/fernet/) method. 
Fernet encryption is an implementation of symmetric(also known as “secret key”) encryption which means that an encrypted message cannot be manipulated or read without the key. There is also a method for decryption in the code that restores the file.

While ransomaware in actual is way more complex, this program covers only the most basic structure.

## :fast_forward: Installation

1. Clone the repository to your local machine.
1. Ensure that Python3 is installed.
1. To encrypt the files, run: `python3 encrypt.py`.
This would encrypt the files `apple-picking.txt` and `dead-leaves.txt`. Note that the code files(`encrypt.py and decrypt.py`) and the key(`thekey.key`) would not be encrypted as a check has been implemented in the code.

1. To decrypt the files, run: `python3 decrypt.py`.
1. Enter the path of the key if placed in other directory than directory of script. If in same directory, then just press enter.
You would get your files back.


## :traffic_light: Usage 
1. View the contents of files: `apple-picking.txt` and `dead-leaves.txt`.
1. Encrypt all files. Run: `encrypt.py`.
1. The `thekey.key` file would be generated when code is run for the first time.
1. Check their content.
1. Decrypt the files. Run: `decrypt.py`.

```bash

# View contents prior to encrytpion
cat dead-leaves.txt

# Encrypt files
python3 encrypt.py

# Decrypt the files
python3 decrypt.py

```


![learn-bas](https://user-images.githubusercontent.com/33151350/170494565-6273f17a-6f9e-42b0-92fa-177f3da308c5.gif)


## :pray: Contributing 
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
## :thumbsup: Credits
This program was built using the tutorial by Network Chuck on Youtube. Check the detailed video [here](https://www.youtube.com/watch?v=UtMMjXOlRQc).

## :warning: Disclaimer: 
- This project aims to provide some exposure to ethical programming. Please do not use it for malicious intents.
- Before running the code, ensure your data is propertly backed up.
- Proceed with caution!
