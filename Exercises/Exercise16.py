'''
Would you like to see a comedy (yes / no)? yes
You might like either Yes Minister or SPAMalot

Another example run:

Would you like to see a comedy (yes / no)? no
Would you like to see a musical (yes / no)? no
You might like either The Woman in Black or Macbeth

Another example run:

Would you like to see a comedy (yes / no)? no
Would you like to see a musical (yes / no)? yes
You might like either Les Miserables or Mamma Mia
'''

comedy=input("Would you like to see a comedy (yes / no)?")
if(comedy.lower()=="yes"):
    print("You might like either Yes Minister or SPAMalot")
elif(comedy.lower()=="no"):
    musical=input("Would you like to see a comedy (yes / no)?")
    if(musical.lower()=="yes"):
        print("You might like either Les Miserables or Mamma Mia")
    elif(musical.lower()=="no"):
        print("You might like either The Woman in Black or Macbeth")
    else:
        print("invalid response")
else:
    print("invalid response")

