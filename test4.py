'''
list = [4,5,6,4,8]
S=[i**2 for i in list]
print(S)

M=[x for x in S if x>50]
print(M)

Given dictionary is consisted of vehicles and their weights in kilograms.
Contruct a list of the names of vehicles with weight below 5000 kilograms.
In the same list comprehension make the key names all upper case.
dict={"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Minivan": 1600, "Van": 2400,
"Semi": 13600, "Bicycle": 7, "Motorcycle": 110}
-----------------------------------------------------------------
Write a Python program to sum all the items in a list
#1
lst = [1,2,3,4,5]
s=0
for i in lst:
    s=s+i
print(s)

Write a Python program to multiply all the items in a list
lst = [1,2,3,4,5]
mt=1
for i in lst:
    mt=mt*i
print(mt)

Write a Python program to get the largest number from a list.
lst = [1,2,3,4,5,8,9,7,6]
lar = lst[0]
for i in lst:
    if(i>lar):
        lar = i
print(lar)

Write a Python program to get the smallest number from a list
lst = [1,2,3,4,5,8,9,7,6,-8]
sm = lst[0]
for i in lst:
    if(i<sm):
        sm = i
print(sm)

Write a Python program to count the number of strings where the string length is 2 or
more and the first and last character are same from a given list of strings
Sample List : ['abc', 'xyz', 'aba', '1221']
Expected Result : 2
lst = ['abc','xyz','aba','1221','uyhtu','ghghghg']
count = 0
for i in lst:
    if(len(i)>2 and (i[0]==i[-1])):
        count=count+1
print(count)

1

1 2 1

1 2 3 2 1

1 2 3 4 3 2 1

1 2 3 4 5 4 3 2 1

rows = 6
for i in range(1, rows + 1):
    for j in range(1, i-1):
        print(j, end=' ')
    for j in range(i-1, 0, -1):
        print(j, end=' ')
    print()

5 4 3 2 1 1 2 3 4 5

5 4 3 2 2 3 4 5

5 4 3 3 4 5

5 4 4 5

5 5
rows = 6
for i in range(0, rows):
    for j in range(rows -1, i, -1):
        print(j, end=" ")
    for k in range(i + 1, rows):
        print(k, end=' ')
    print('\n')

from functools import reduce

lst = [1,2,3,4,5]
sum = reduce(lambda a, b: a+b, lst)
print(sum)
'''

class University:
    def updateMarks(self):
        print("Marks = 1")

class Student(University):
    def updateMarks(self):
        print("Marks = 100")

obj1 = University()
obj2 = Student()
obj1.updateMarks()
obj2.updateMarks()









