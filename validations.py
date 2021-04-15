
import re #re module provides support for regular Expressions
def isEmailExists(email):
    pass

def isEmailValid(email):
    pass

def isUserSessionValid(accountNumber):
    pass

def isFieldEmpty(field):
    return True if field else False

def isEmailFormatValid(email):
    emailRegEx = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
    return True if re.search(emailRegEx,email) else False
   
'''
Verify if password length is atleast 3 charaters
'''
def isPasswordValid(password):
    return True if len(password)>=3 else False

def validationfieldSummary(fieldValueDict):
    fieldErrorList = []
    #empty field validations
    for key,value in fieldValueDict.items():
        if not isFieldEmpty(value):
            fieldErrorList.append('{0} cannot be empty'.format(key))
    return fieldErrorList
        

    
    
    
        
    
    