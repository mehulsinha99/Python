'''
Write a Python program that accepts a string and calculate the number of digits and letters.
Sample Data : Python 3.2
Expected Output :
Letters 6  65,90
Digits 2  48 57
'''
#extra2
data= input("Input : ")
countLetter=0
countDigit=0
for i in data:
    if(ord(i)>=65 and ord(i)<122):
        countLetter+=1
    elif(ord(i)>=48 and ord(i)<58):
        countDigit+=1
print("Letters = ",countLetter)
print("Digits = ",countDigit)
