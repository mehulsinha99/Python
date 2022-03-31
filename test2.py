'''import sys

for path in sys.path:
    print(path)
    print()
'''

def greet(*names):
    for name in names:
        print("hello",name)

#greet("mehul","nikhil","asif","rehan")

count = 5
def some_method():
    global count
    count+=1
    print("Inner",count)
some_method()
print("Outer",count)

#filter, map, sort, reduce functions

print(eval("2+2"))


