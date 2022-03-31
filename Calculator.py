def add(n1,n2):
    print(n1+n2)

def subtract(n1,n2):
    print(n1-n2)

def multiply(n1,n2):
    print(n1*n2)

def divide(n1,n2):
    if(n2==0):
        print("cannot divide by 0")
    else:
        print(n1/n2)

for i in range(0,3):
    print("Select Operation: \n1.Add\n2.Subtract\n3.Multiply\n4.Divide")
    ch = int(input("Enter Choice[1/2/3/4]"))
    if(ch==1):
        num1 = float(input("enter 1st num:"))
        num2 = float(input("enter 2nd num:"))
        add(num1,num2)
    elif(ch==2):
        num1 = float(input("enter 1st num:"))
        num2 = float(input("enter 2nd num:"))
        subtract(num1, num2)
    elif (ch == 3):
        num1 = float(input("enter 1st num:"))
        num2 = float(input("enter 2nd num:"))
        multiply(num1, num2)
    elif (ch == 4):
        num1 = float(input("enter 1st num:"))
        num2 = float(input("enter 2nd num:"))
        divide(num1, num2)
    else:
        print("invalid choice")
