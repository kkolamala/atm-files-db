import sys
import os
import json #module makes it easy to parse JSON strings and files containing JSON object

directoryPath = './database/'
sessionDirectory = './auth_session/'
filePath = os.path.join(directoryPath,"bankDB.json")

def createFile(userDetails):
    try:
        if(path.exists(filePath)):
            #read the data from file and append the new data
            data = readFile(filePath)
            userDetails.update(data)
        with open(filePath,'w') as outfile:
            json.dump(userDetails,outfile)
    except:
        error = sys.exc_info()[0]
        print('exception occured adding data to file - ',error )

def createSessionFile(accountNumber):
    fileName = accountNumber + '.txt'
    sessionFilepath = os.path.join(sessionDirectory,fileName)
    with open(sessionFilepath,'w') as outfile:
        json.dump(accountNumber,outfile)
    
def readFile(fileName='./database/bankDB.json'):
    data = {}
    with open(fileName) as userData:
        data = json.load(userData)
    return data
    

def deleteFile(accountNumber):
    isDeleteSuccessful = False
    fileName = accountNumber + '.txt'
    sessionFile = os.path.join(sessionDirectory,fileName)
    if os.path.exists(sessionFile):
        try:
            os.remove(sessionFile)
            isDeleteSuccessful = True
            return isDeleteSuccessful
        except:
            error = sys.exc_info()[0]
            print('exception occured adding data to file - ',error )
        finally:
            return isDeleteSuccessful
        
        
            

def updateFile(accountNumber,data):
    usersData = readFile();
    usersData[accountNumber] = data
    with open(filePath,'w') as outfile:
        json.dump(usersData,outfile)
    

