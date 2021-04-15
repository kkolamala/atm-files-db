import validations
import utility
import sys
sys.path.append("./database")
bankName = 'ABC Bank'
import accountAPI

print(' ************************ ')
print('   Welcome to  %s'% bankName)
print(' ************************ ')

def login():
    print('welcome to login page')
    accountNumber = input('Enter Account Numebr :')
    password = input('Enter Password')
    accountDetailsResponse = accountAPI.verifyAccount(accountNumber,password)
    if(type(accountDetailsResponse) is dict):
        print('login successful')
        userData = accountDetailsResponse[accountNumber]
        balance = userData['balance']
        bankOPerations(accountNumber,balance)
    else:
        print(accountDetailsResponse)
        
def bankOPerations(accountNumber,balance):
    print('What would you like to do? 1.withdraw \n 2.Deposit \n 3.balance check \n 4.complaint issue 5.Close Account')
    selectedOption = input('Please select an option: ')
    
    if(selectedOption == '1'):
        withdraw(accountNumber)
            
    if(selectedOption == '2'):
        deposit()
        
    if(selectedOption == '3'):
        balanceCheck()
            
    if(selectedOption == '4'):
        registerComplaint()
            
    if(selectedOption == '5'):
        closeAccount()
        
        
def registerFields():
    fNmae = input('Enter First Name :')
    lName = input('Enter Last Name :')
    email = input('Enter Email :')
    password = input('Enter Password (minimum of 3 characters length):')
    fieldValueDict = {}
    fieldValueDict['FirstName'] = fNmae
    fieldValueDict['LastName'] = lName
    fieldValueDict['Email'] = email
    fieldValueDict['Password'] = password
    return fieldValueDict

def handleRegisterFieldErrors(fieldValueDict):
    fieldErrors = []
    fieldErrors = validations.validationfieldSummary(fieldValueDict)
    
    if not validations.isEmailFormatValid(fieldValueDict['Email']) and fieldValueDict['Email']:
        fieldErrors.append('Email format is not valid')
    
    if not validations.isPasswordValid(fieldValueDict['Password']) and fieldValueDict['Password']:
        fieldErrors.append('Password cannot be less than 3 characters')
        
    return fieldErrors
    

def register():
    print('welcome to register page')
    
    fieldValueDict = registerFields()
    
    fieldErrors = handleRegisterFieldErrors(fieldValueDict)
    
    if(len(fieldErrors) > 0):
        print(fieldErrors)
    else:
        userDetailsDict= {}
        accountNumber = utility.randomNumberGenerate()
        fieldValueDict["balance"] = 0;
        userDetailsDict[accountNumber] = fieldValueDict
        try:
            accountAPI.createAccount(userDetailsDict)
            print('Registration is successful. Account Number - %d'% accountNumber )
        except:
            print('error registering user')
    

def init():
    print('for login enter 1 ')
    print('for register enter 2',end =" ")
    userChoice = input(':')
    try:
        isUserChoiceValid = False
        while not isUserChoiceValid:
            userChoice = int(userChoice)
            if(userChoice in [1,2]):
                isUserChoiceValid = True
                if(userChoice == 1):
                    login()
                    break
                else:
                    register()
                    break
            else:
                print('choose between 1 and 2')
                userChoice = input('choose option: ' )
    except:
        print('invalid option entered')



init()

#print(accountAPI.ping())



