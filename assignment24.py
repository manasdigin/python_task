import math
def triangle ():
    x=int(input("enter x:"))
    y=int(input("enter y:"))
    z=int(input("enter z:"))
    s = (x + y+ z)/ 2  
    area =math.sqrt(s * (s - x) * (s - y) * (s - z))
    print("area of triangle:",area)
triangle()

print("-------------------------__________------------------------")

def square():
    a=int(input("enter number"))
    area_square=a*a
    print("area of square is",area_square)
square()

print("_________________________________________________")


def rectangle ():
    length=float(input("enter the length"))
    breadth=float(input("enter the breadth"))
    area_rectangle=length*breadth
    print("area of rectangle is:",area_rectangle)
rectangle()

print("______________+++++++++++++++)))))))))****")


def circle():
    r=float(input("enter radius"))
    r=3.149*r*r
    print("area of circle is:",r)
circle()

print('++++++++++++++++++++++++++++++++++++++++++++++++++++')


def trapezium():
    base1=float(input("write base 1"))
    base2=float(input("write base2"))
    height=float(input("height:"))
    area_trapezium=((base1+base2)/2)*height
    print("area of trapezium is",area_trapezium)
trapezium()