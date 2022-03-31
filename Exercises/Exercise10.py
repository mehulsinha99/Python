'''
A three-day festival is the official celebration of all things of “Doctor Who”.
There are three categories of tickets: individual cost is £68, under sixteen is £32.25 and a family cost 42.75.
Write a program that asks the user for total numbers in each category,
calculate and display the breakdown of each and total prices.
To get more idea please see the execution of the program below:

Doctor Who Festival - Price Calculator
Note: enter 0 if none

Enter total number of individuals : 3
Enter total number of under 16s: 2
Enter total number of families : 1

Category Price Breakdown:
Price is £204 for 3 individuals
Price is £64.5 for 2 under 16s
Price is £42.75 for 1 families

Total Persons are 9
Total Event Price is £311.25
More info and booking visit our website

'''

print("Doctor Who Festival - Price Calculator\nNote: enter 0 if none")
individual = int(input("Enter total number of individuals: "))
under16 = int(input("Enter total number of under 16s: "))
family = int(input("Enter total number of families: "))

individualPrice = 68
underSixteenPrice = 32.25
familyPrice = 42.75

totalIndividualCost = individual*individualPrice
totalUnderCost = under16*underSixteenPrice
totalFamilyCost = family*familyPrice

print("\nCategory Price Breakdown: ")
print("Price is",totalIndividualCost,"for",individual,"individuals")
print("Price is",totalUnderCost,"for",under16,"under 16s")
print("Price is",totalFamilyCost,"for",family,"families")
total = totalIndividualCost + totalUnderCost + totalFamilyCost
totalPerson = individual + under16 + (family*4)
print("\nTotal Persons are",totalPerson)
print("Total Event Price is",total)
print("More info and booking visit our website")
