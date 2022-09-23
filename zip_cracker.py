#!/usr/bin/env python3
from pathlib import Path
import zipfile
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
    try:
        zipFile.extractall(pwd=bytes(password, 'utf-8'))
        return password
    except:
        return

def main():
    zipFile = sys.argv[1]
    wordlist = sys.argv[2]

    zipVerification = zipfile.is_zipfile(zipFile)
    textFileVerification = os.path.splitext(wordlist)[-1].lower()

    if zipVerification == True:
        zipFile = zipfile.ZipFile(sys.argv[1])
    else:
        print("[!] Type a valid Zip file")

        
    if textFileVerification == ".txt":
        textFileVerification = wordlist
        wordlist = open(wordlist)
    else:
        print("[!] Write an existing text file")
        
    for line in wordlist.readlines():
        password = line.strip("\n")
        crack = extractZip(zipFile, password)
        if crack:
            print("[+] The password is: " + password)
            break

if __name__ == '__main__':
    main()