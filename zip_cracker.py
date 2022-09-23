#!/usr/bin/env python3

# Importing the libraries
from pathlib import Path
import pyzipper
import sys
import os

# Correct Execution
if len(sys.argv) != 3:
    print("[!] Correct execution: python3 %s [zipfile] [wordlist]"%(sys.argv[0]))
    sys.exit(0)

print(r"""
 ______          ____                _             
|__  (_)_ __    / ___|_ __ __ _  ___| | _____ _ __ 
  / /| | '_ \  | |   | '__/ _` |/ __| |/ / _ \ '__|
 / /_| | |_) | | |___| | | (_| | (__|   <  __/ |   
/____|_| .__/___\____|_|  \__,_|\___|_|\_\___|_|   
       |_| |_____|                                 
""")

# Fuction to extract the content of the Zip File
def extractZip(zipFile, password):
    with pyzipper.AESZipFile(zipFile, 'r') as zipFile:
        try:
            zipFile.extractall(pwd=bytes(password, 'ASCII'))
            return password
        except:
            return

def main():
    zipFile = sys.argv[1]
    wordlist = sys.argv[2]

    # Making the verification of the text and zip file
    textFileVerification = os.path.splitext(wordlist)[-1].lower()
    zipVerification = pyzipper.is_zipfile(zipFile)

    if zipVerification == False:
        print("[!] Type a valid Zip file")
        return

    if textFileVerification == ".txt":
        textFileVerification = wordlist
        wordlist = open(wordlist)
    else:
        print("[!] Type a valid text file")

    print("[+] Starting the crack...")

    # For loop to make the crack
    for line in wordlist.readlines():
        password = line.strip('\n')
        crack = extractZip(zipFile, password)
        if crack:
            print("[+] The password is: " + password)
            break
    if crack == None:
        print("[!] Reached the end of the wordlist and couldn't crack the password")

if __name__ == '__main__':
    main()