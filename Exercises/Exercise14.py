'''

A certain cinema currently sells tickets for a full price of 6 pounds,
but always sells tickets for half price to people who are less than 16 years old,
and for a third of the price for people who are 60 years old or more.
An example run of the program (numbers in bold are typed in by the user)

Enter your age: 63
Your ticket costs £2.00

'''
age = int(input("Enter your age: "))
fullPrice = 6.0
if(age<16 and age>=0):
    print("Your ticket costs £","{0:.2f}".format(fullPrice/2))
elif(age>60):
    print("Your ticket costs £","{0:.2f}".format(fullPrice/3))
elif(age<0):
    print("Invalid age")
else:
    print("Your ticket costs £", "{0:.2f}".format(fullPrice))
