'''
Write a program that reads an integer value between 1 and 12 from the user and prints output the corresponding month of the year.

An example run of the program (numbers in bold are typed in by the user)

Enter the month: 3
Month 3 is March

'''
num= int(input("Enter the month: "))
if(num==1):
    print("Month",num,"is January")
elif(num==2):
    print("Month",num,"is February")
elif(num==3):
    print("Month",num,"is March")
elif(num==4):
    print("Month",num,"is April")
elif(num==5):
    print("Month",num,"is May")
elif(num==6):
    print("Month",num,"is June")
elif(num==7):
    print("Month",num,"is July")
elif(num==8):
    print("Month",num,"is August")
elif(num==9):
    print("Month",num,"is September")
elif(num==10):
    print("Month",num,"is October")
elif(num==11):
    print("Month",num,"is November")
elif(num==12):
    print("Month",num,"is December")
else:
    print("Invalid month number")