'''
Write a program that reads an integer value from the user and prints output whether it is odd or even.

An example run of the program (numbers in bold are typed in by the user)

Enter a number: 13
13 is “even”


'''
num=int(input("Enter a number: "))
if(num%2==0):
    print(num,'is "even"')
else:
    print(num, 'is "odd"')