import math as m

class Shape:
    def area(self):
        print("-------Area of your shape:")

class Circle(Shape):

    def area(self,radius):
        Shape.area(self)
        area = m.pi * (radius ** 2)
        return area

class Square(Shape):

    def area(self,len):
        Shape.area(self)
        area = len ** 2
        return area
obj1 = Circle()
obj2 = Square()
while(True):
    print("Choose your shape: \n1.Circle\n2.Square\nPress 0 to exit")
    choice = int(input("Enter your choice:"))
    if(choice==1):
        radius = float(input("Enter Radius: "))
        print(obj1.area(radius))
    elif(choice==2):
        len = float(input("Enter length: "))
        print(obj2.area(len))
    elif(choice==0):
        break
    else:
        print("Invalid choice")

