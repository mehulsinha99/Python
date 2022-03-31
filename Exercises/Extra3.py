'''
Write a Python program to check the validity of password input by users. Go to the editor
Validation :

At least 1 letter between [a-z] and 1 letter between [A-Z].   65-90 && 97-122
At least 1 number between [0-9].                              48-57
At least 1 character from [$#@].                              35,36,64
Minimum length 6 characters.
Maximum length 16 characters.

'''

password = input("Enter password: ")
lenghtOfPassword = len(password)
lenFlag = False
capLetterFlag = False
charFlag = False
numFlag = False
smallLetterFlag = False
if(lenghtOfPassword>=6 and lenghtOfPassword<17):
    lenFlag = True

for i in password:
    if(ord(i)>=65 and ord(i)<91):
        capLetterFlag = True
    if(ord(i)>=97 and ord(i)<123):
        smallLetterFlag = True
    if(ord(i)>=48 and ord(i)<58):
        numFlag = True
    if(ord(i)==35 or ord(i)==36 or ord(i)==64):
        charFlag = True

if(lenFlag and capLetterFlag and smallLetterFlag and numFlag and charFlag == True):
    print("Strong password")
else:
    print("Weak password")
#----------------------------------------------
if(lenFlag==False):
    print("Lenght should be in between 6-16, Your length",lenghtOfPassword)
if(capLetterFlag==False):
    print("At least 1 letter between [A-Z]")
if(smallLetterFlag==False):
    print("At least 1 letter between [a-z]")
if(numFlag==False):
    print("At least 1 number between [0-9]")
if(charFlag==False):
    print("At least one special character required")