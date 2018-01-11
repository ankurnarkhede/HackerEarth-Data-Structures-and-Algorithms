#-----area perimeter-------
def square(s=3):
    "area  and perimeter of square"
    A=s*s
    P=4*s
    print "area of square is",A,"perimeter of square is",P
    return;
    
def circle(r=2):
    "area perimeter of circle"
    A=3.14*r*r
    P=2*3.14*r
    print "area of circle is",A,"perimeter of circle is",P
    return;
    
def tri(b=2, h=2, s1=2, s2=2, s3=2):
    "area perimeter of circle"
    A=0.5*b*h
    P=s1+s2+s3
    print "area of triangle is",A,"perimeter of triangle is",P
    return;
    
    
    
#-----main---------
s=int(input("input side of sq"))
square()

r=int(input("input radius of circle"))
circle()


b=int(input("input breadth of circle"))
h=int(input("input height of circle"))
s1=int(input("input radius of circle"))
s2=int(input("input radius of circle"))
s3=int(input("input radius of circle"))
tri()
