import sys
sys.path.append("./database")
import fileUtility 

filePath = './database/bankDB.json'

def createAccount(userDetails):
    try:
        fileUtility.createFile(userDetails)
    except:
        error = sys.exc_info()[0]
        print('exception occured while creating account - ',error )
        
def verifyAccount(accountNumber,password):
    accountDict = {}
    message = ' '
    isAccountValid = False
    isPasswordValid = False
    
    userDict = fileUtility.readFile(filePath)
    
    for key,value in userDict.items():
        if(key == accountNumber):
            isAccountValid = True
            if(value['Password'] == password):
                isPasswordValid = True
                accountDict[key] = value
                
    if accountDict and isAccountValid and isPasswordValid:
        #creation a file in session for the user
        fileUtility.createSessionFile(accountNumber)
        return accountDict
    elif not isAccountValid :
        return 'Invalid Account Number'  
    elif not isPasswordValid:
        return 'Invalid Password' 
    
def getAccountDetailsByAccountNumber(accountNumber):
    usersDict = fileUtility.readFile(filePath)
    userDict = {}
    for key,value in usersDict.items():
        if(key == accountNumber):
            userDict[key] = value
            return userDict

def deleteAccount(accountNumber):
    pass


def ping():
    return 'ping from Account API'


