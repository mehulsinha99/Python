'''
    *
   **
  ***
 ****
*****
k = 8
for i in range(0, 5):
    for j in range(0, k):
        print(end=" ")
    k = k - 2
    for j in range(0, i + 1):
        print("* ", end="")
    print("")
'''

'''
1
12
123
1234
12345

count=1
for i in range(1,6):
    for j in range(1,i+1):
        print(count,end=' ')
        count+=1
    print()
    
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


A 
B B 
C C C 
D D D D 
E E E E E
'''
num=65
for i in range(1,6):
    for j in range(1,i+1):
        print(chr(num),end=' ')
    num+=1
    print()


