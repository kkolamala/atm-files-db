import sys
sys.path.append("./database")
import bankOperationsAPI 

def deposit(accountNumber):
    depositAmount = input('Enter amount to deposit: ')
    bankOperationsAPI.depositAmount(accountNumber,depositAmount)
    
def withdraw(accountNumber):
    withdrawAmount = int(input('Enter amount to withdraw'))
    balance = int(bankOperationsAPI.getBalance(accountNumber))
    if withdrawAmount > balance :
        print('your withdrawl amount $ %d exceeds available balance - $ %d'%(withdrawAmount,balance))
    else:
        try:
            #reduce the withdrawl amount from balance
            balanceAfterWithdrawl = balance - withdrawAmount
            bankOperationsAPI.depositAmount(accountNumber,balanceAfterWithdrawl)
            print('Take your cash $ %d'% withdrawAmount)
        except:
            print('some error occured withdrawign cash')
        
        
    
def balanceCheck(accountNumber):
    balance = bankOperationsAPI.getBalance(accountNumber)
    print('balance is - $ %s'% balance)
    
def registerComplaint(accountNumber):
    complaint = input('enter your complaint: ')
    print('your complaint is registered. will get back to you soon')

def closeAccount(accountNumber):
    print('your account closed')
    