import sys
import os.path
from os import path
import json #module makes it easy to parse JSON strings and files containing JSON object

directoryPath = './database/'

def createFile(userDetails):
    try:
        filePath = os.path.join(directoryPath,"bankDB.json")
        if(path.exists(filePath)):
            #read the data from file and append the new data
            data = readFile(filePath)
            userDetails.update(data)
        with open(filePath,'w') as outfile:
            json.dump(userDetails,outfile)
    except:
        error = sys.exc_info()[0]
        print('exception occured adding data to file - ',error )
        

def readFile(fileName):
    data = {}
    with open(fileName) as userData:
        data = json.load(userData)
    return data
    

def deleteFile(fileName):
    pass

def updateFile(fileName,data):
    pass

