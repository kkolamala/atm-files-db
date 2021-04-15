import sys
sys.path.append("./database")
import fileUtility 
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
    filePath = './database/bankDB.json'
    userDict = fileUtility.readFile(filePath)
    
    for key,value in userDict.items():
        if(key == accountNumber):
            isAccountValid = True
            if(value['Password'] == password):
                isPasswordValid = True
                accountDict[key] = value
                return accountDict
    if accountDict:
        return accountDict
    elif not isAccountValid :
        return 'Invalid Account Number'  
    elif not isPasswordValid:
        return 'Invalid Password'  

def deleteAccount(accountNumber):
    pass


def ping():
    return 'ping from Account API'


