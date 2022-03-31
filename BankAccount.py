class BankAccount:

    def __init__(self,consumerName,accNum,balance):
        self.consumerName = consumerName
        self.accNum = accNum
        self.balance = balance
    def withdrawMoney(self,amountToWithdraw):
        if(self.balance>=amountToWithdraw):
            self.balance -= amountToWithdraw
            print("Amount Deducted, Your current balance is :",self.balance)
        else:
            print("Insufficient Balance, Please add some money")
    def depositMoney(self,amountToDeposit):
        self.balance+=amountToDeposit
        print("Amount deposited, Your current balance is :",self.balance)
    def transferDeposit(self,amountTransferred):
        self.balance+=amountTransferred
        print("Amount transferred: ",amountTransferred)
    def payBill(self,billAmount):
        if(self.balance>=billAmount):
            self.balance -= billAmount
            print("Bill Paid!!!")
        else:
            print("Insufficient balance for the bill")
    def getBalance(self):
        print(self.balance)


Acc1 = BankAccount("Dennis Ritchie","45000903",1000)
Acc2 = BankAccount("Guido Rossum","45000904",1000)
Acc3 = BankAccount("James Goslin","45000905",1000)
while(True):
    print("List of Users:\n1. Dennis Ritchie\n2. Guido Rossum\n3. James Goslin\nPress 9 to exit")
    op = int(input("Choose user: "))
    if(op==1):
        # ----------------------------------------------------------------------------------
        print("--------------------------------------WELCOME TO HDFC BANK--------------------------------------")
        print("Acc holder's name: " + Acc1.consumerName + " | Account Number: ", Acc1.accNum, " | Account Balance: ",
              end="")
        Acc1.getBalance()
        print("************************************************************************************************")

        while (True):
            print("1. Withdraw Money\n2. Deposit Money\n3. Transfer Funds\n4. Pay Credit Card Bill\nPress 0 to exit")
            choice = int(input("Enter your choice: "))
            if (choice == 1):
                withdrawAmount = float(input("Enter amount you want to withdraw :"))
                Acc1.withdrawMoney(withdrawAmount)

            elif (choice == 2):
                depositAmount = float(input("Enter amount you want to deposit :"))
                Acc1.depositMoney(depositAmount)
            elif(choice==3):
                print("List of Beneficiary\n1. Guido Rossum\n2. James Goslin")
                n=int(input("Choose beneficiary:"))
                if(n==1):
                    amt = float(input("Enter Amount to transfer: "))
                    if(Acc1.balance>=amt):
                        Acc1.withdrawMoney(amt)
                        Acc2.transferDeposit(amt)
                    else:
                        print("Transfer Failed........")
                elif(n==2):
                    amt = float(input("Enter Amount to transfer: "))
                    if (Acc1.balance >= amt):
                        Acc1.withdrawMoney(amt)
                        Acc3.transferDeposit(amt)
                    else:
                        print("Transfer Failed........")
                else:
                    print("Invalid choice")

            elif(choice==4):
                print("Pay your bill for CrCard# 4824 1234 8645 4563")
                billAmt = float(input("Enter Bill amount:"))
                Acc1.payBill(billAmt)
            elif (choice == 0):
                print("Thank you for banking with us. Have a nice day!")
                break
            else:
                print("Invalid Choice.. Please try again!")
        # -------------------------------------------------------------------------------------
    elif(op==2):
        # ----------------------------------------------------------------------------------
        print("--------------------------------------WELCOME TO HDFC BANK--------------------------------------")
        print("Acc holder's name: " + Acc2.consumerName + " | Account Number: ", Acc2.accNum, " | Account Balance: ",
              end="")
        Acc2.getBalance()
        print("************************************************************************************************")

        while (True):
            print("1. Withdraw Money\n2. Deposit Money\n3. Transfer Funds\n4. Pay Credit Card Bill\nPress 0 to exit")
            choice2 = int(input("Enter your choice: "))
            if (choice2 == 1):
                withdrawAmount = float(input("Enter amount you want to withdraw :"))
                Acc2.withdrawMoney(withdrawAmount)

            elif (choice2 == 2):
                depositAmount = float(input("Enter amount you want to deposit :"))
                Acc2.depositMoney(depositAmount)

            elif (choice2 == 3):
                print("List of Beneficiary\n1. Dennis Ritchie\n2. James Goslin")
                n1 = int(input("Choose beneficiary:"))
                if (n1 == 1):

                    amt = float(input("Enter Amount to transfer: "))
                    if(Acc2.balance>=amt):
                        Acc2.withdrawMoney(amt)
                        Acc1.transferDeposit(amt)
                    else:
                        print("Transfer Failed.......")
                elif(n1 == 2):
                    amt = float(input("Enter Amount to transfer: "))
                    if (Acc2.balance >= amt):
                        Acc2.withdrawMoney(amt)
                        Acc3.transferDeposit(amt)
                    else:
                        print("Transfer Failed.......")
                else:
                    print("Invalid choice")

            elif (choice2 == 4):
                print("Pay your bill for CrCard# 4815 5234 9852 7563")
                billAmt = float(input("Enter Bill amount:"))
                Acc2.payBill(billAmt)

            elif (choice2 == 0):
                print("Thank you for banking with us. Have a nice day!")
                break

            else:
                print("Invalid Choice.. Please try again!")
        # -------------------------------------------------------------------------------------

    elif(op==3):
        # ----------------------------------------------------------------------------------
        print("--------------------------------------WELCOME TO HDFC BANK--------------------------------------")
        print("Acc holder's name: " + Acc3.consumerName + " | Account Number: ", Acc3.accNum, " | Account Balance: ",
              end="")
        Acc3.getBalance()
        print("************************************************************************************************")

        while (True):
            print("1. Withdraw Money\n2. Deposit Money\n3. Transfer Funds\n4. Pay Credit Card Bill\nPress 0 to exit")
            choice3 = int(input("Enter your choice: "))
            if (choice3 == 1):
                withdrawAmount = float(input("Enter amount you want to withdraw :"))
                Acc3.withdrawMoney(withdrawAmount)

            elif (choice3 == 2):
                depositAmount = float(input("Enter amount you want to deposit :"))
                Acc3.depositMoney(depositAmount)

            elif (choice3 == 3):
                print("List of Beneficiary\n1. Dennis Ritchie\n2. Guido Rossum")
                n2 = int(input("Choose beneficiary:"))
                if (n2 == 1):
                    amt = float(input("Enter Amount to transfer: "))
                    if(Acc3.balance>=amt):
                        Acc3.withdrawMoney(amt)
                        Acc1.transferDeposit(amt)
                    else:
                        print("Transfer Failed.........")
                elif (n2 == 2):
                    amt = float(input("Enter Amount to transfer: "))
                    if (Acc3.balance >= amt):
                        Acc3.withdrawMoney(amt)
                        Acc2.transferDeposit(amt)
                    else:
                        print("Transfer Failed.........")
                else:
                    print("Invalid choice")

            elif (choice3 == 4):
                print("Pay your bill for CrCard# 9815 5234 9852 7563")
                billAmt = float(input("Enter Bill amount:"))
                Acc3.payBill(billAmt)

            elif (choice3 == 0):
                print("Thank you for banking with us. Have a nice day!")
                break

            else:
                print("Invalid Choice.. Please try again!")
        # -------------------------------------------------------------------------------------
    elif(op==9):
        break
    else:
        print("Invalid Choice.. Please try again!")



