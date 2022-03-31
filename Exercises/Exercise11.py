'''
Please enter your first name: Peter
Please enter your last name: Cambridge
Your full name is PETER CAMBRIDGE
Your initials are P C
First name length is 5 letters
Last name length is 9 letters
Full name length is 14 letters
First name starts with P
First name ends with R
Last name starts with C
Last name ends with E
First name indexes are 0 – 4
Last name indexes are 0 – 8
First name trims 1 Pet
First name trims 2 eter
Last name trims 1 Cam
Last name trims 2 bridge
'''
firstName = input("Please enter your first name: ")
lastName = input("Please enter your last name: ")
fNameUpper = firstName.upper()
lNameUpper = lastName.upper()
print("Your full name is",fNameUpper,lNameUpper)
print("Your initials are",fNameUpper[0:1],lNameUpper[0:1])
print("First name length is",len(firstName),"letters")
print("Last name length is",len(lastName),"letters")
print("Full name length is",len(firstName)+len(lastName),"letters")
print("First name starts with",fNameUpper[0:1])
print("First name ends with",fNameUpper[-1:-2:-1])
print("Last name starts with",lNameUpper[0:1])
print("Last name ends with",lNameUpper[-1:-2:-1])
print("First name indexes are 0 –",len(firstName)-1)
print("Last name indexes are 0 – ",len(lastName)-1)
print("First name trims 1",firstName[0:3])
print("First name trims 2",firstName[1:])
print("Last name trims 1",lastName[0:3])
print("Last name trims 2",lastName[3:])
