'''
Write a program that asks the user to enter his/her name and then partly encrypt and display it.

An example run of the program (text in bold are typed in by the user)

Please enter your name: Jimmy
Encrypted form is J***y
--------------------
name = input("Please enter your name: ")

for i in range(1, lengthOfName-1):
    name = name.replace(name[i], "*")
print(lengthOfName)
print(name)
-----------------
name = input("Please Enter your name: ")
counter = 0
newName = ''
for x in name:
    if(counter != 0 and counter != len(name)-1):
        x = 'x'
    else:
        pass
    counter = counter+1
    newName = newName+x
print(f"Encrypted Form is :{newName}")
'''
#ex21
name = input("Please enter your name: ")
lengthOfName = len(name)
name = name.replace(name[1:-1], "*"*(lengthOfName-2))
print(lengthOfName)
print(name)


