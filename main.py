import sys
import requests

url = None
wordlist = None
dirMode = False
subdMode = False
output = False
outputFile = None


for i in sys.argv:
    if sys.argv[i] == "-u":
        targetUrl = sys.argv[i+1]
    elif sys.argv[i] == "-w":
       selectedWordlist = sys.argv[i+1]
    elif sys.argv[i] == "dir":
        dirMode = True
    elif sys.argv[i] == "subd":
        subdMode = True
    elif sys.argv[i] == "-o":
        output = True
        outputFile = sys.argv[i+1] 


def dirMode(url,wordlist,shouldOutput,outputFile):

    url = url
    wordlist = wordlist
    goodDirs = []
    while True:
        with open(f"{wordlist}","r") as wordlistFile:
            readWordlist = wordlistFile.readlines()

            for directory in readWordlist:
                baseWithDir = f"{url}/{directory}"

                testLink = requests.get(baseWithDir)

                if testLink.status_code == 200 or testLink.status_code == 201 or testLink.status_code == 202 or testLink.status_code == 204 or testLink.status_code == 304:
                    goodDirs.append(baseWithDir)

                if not readWordlist:
                    break

        for dirs in goodDirs:
            
            print(f"--> {dirs}\n")

            if shouldOutput == True:
                with open(f"{outputFile}","a") as filetoOutputInto:
                   writeToOutputFile = filetoOutputInto.write(dirs)

            

def subdMode(url,wordlist,shouldOutput,outputFile):

    url = url
    wordlist = wordlist
    
    goodDirs = []

    if url.startswith("http://"):
        url = url.replace("http://","")
        url = f"{url}"
    while True:
        with open(f"{wordlist}","r") as wordlistFile:
            readWordlist = wordlistFile.readlines()

            for subd in readWordlist:

                subdWithDir = f"https://{subd}.{url}"
                testLink = requests.get(subdWithDir)

                if testLink.status_code == 200 or testLink.status_code == 201 or testLink.status_code == 202 or testLink.status_code == 204 or testLink.status_code == 304:
                    goodDirs.append(subdWithDir)

                if not readWordlist:
                    break

        for dirs in goodDirs:
            
            print(f"--> {dirs}\n")

            if shouldOutput == True:
                with open(f"{outputFile}","a") as filetoOutputInto:
                   writeToOutputFile = filetoOutputInto.write(dirs)
                
   

if dirMode == True:
    dirMode(targetUrl,selectedWordlist,output,outputFile)

elif subdMode == True:
    subdMode(targetUrl,selectedWordlist,output,outputFile)