import sys
sys.path.append("./database")
import fileUtility 
import accountAPI

def getBalance(accountNumber):
     #get balance for account number
    try:
        userDict = {}
        userDict = accountAPI.getAccountDetailsByAccountNumber(accountNumber)
        balance = userDict[accountNumber]['balance']
        return balance 
    except:
        error = sys.exc_info()[0]
        print('exception occured while creating account - ',error )

def depositAmount(accountNumber,amountToDeposit):
    #get user account details
    try:
        userDict = {}
        userDict = accountAPI.getAccountDetailsByAccountNumber(accountNumber)
        userDict[accountNumber]['balance'] = amountToDeposit
        fileUtility.updateFile(accountNumber,userDict[accountNumber]) 
    except:
        error = sys.exc_info()[0]
        print('exception occured while creating account - ',error )
        
    

def withdrawAmount(accountNumber,amountToWithdraw):
    pass


