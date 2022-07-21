from pathlib import Path
import zipfile
import sys
import os

if len(sys.argv) != 3:
    print("[!] Correct execution: python3 %s [zipfile] [wordlist]"%(sys.argv[0]))
    sys.exit(0)

def extractZip(zipFile, password):
    try:
        zipFile.extractall(pwd=bytes(password, 'utf-8'))
        return password
    except:
        return

def main():
    zipFile = sys.argv[1]
    wordlist = sys.argv[2]
    textFileVerification = os.path.splitext(wordlist)[-1].lower()
    zipVerification = zipfile.is_zipfile(zipFile)
    if zipVerification == True:
        zipFile = zipfile.ZipFile(sys.argv[1])
    else:
        print("[!] Write an existing Zip file")
    if textFileVerification == ".txt":
            textFileVerification = wordlist
            wordlist = open(wordlist)
    else:
        print("[!] Write an existing text file") 
    for line in wordlist.readlines():
        password = line.strip("\n")
        crack = extractZip(zipFile, password)
        if crack:
            print("[!] The password is: " + password)
            break
        else:
            print("[!] Reached the end of wordlist!")

if __name__ == '__main__':
    main()
