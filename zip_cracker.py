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

    zipVerification = zipfile.is_zipfile(zipFile)
    textFileVerification = os.path.splitext(wordlist)

    if zipVerification == True:
        zipFile = zipfile.ZipFile(sys.argv[1])
    else:
        print("[!] Type a valid Zip file")
        
    if textFileVerification[1] == ".txt":
        textFileVerification = wordlist
        wordlist = open(wordlist)
    else:
        print("[!] Type a valid text file")
        
    for line in wordlist.readlines():
        password = line.strip("\n")
        crack = extractZip(zipFile, password)
        if crack:
            print("[+] The password is: " + password)
            break
        else:
            print("[!] Reached the end of wordlist!")
            break

if __name__ == '__main__':
    main()
