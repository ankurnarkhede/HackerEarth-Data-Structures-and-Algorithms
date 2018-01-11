#-----inheritance----
#to add
class A():
    def __init__(self):
        print "this is A const"
        
    def A_add(self,a,b):
        return a+b,a-b
m=A()
#to subtract
class B():
    def __init__(self):
        print "this is B const"
        
    def B_mul(self,a,b):
        return a*b,a/b
        
#call both
class C(A,B):
    def __init__(self):
        print "this is C const"
    
    
    
        
n=C()
#a=int(input("enter a:"))
#b=int(input("enter b:"))
[add,sub]=n.A_add(5,9)
print "add:",add,"\nsub:",sub      
[mul,div]=n.B_mul(5,9)
print "mul:",mul,"\ndiv:",div      



#----issubclass isinstance
print issubclass(C,A)   #issubclass(subclass,superclass)....returns boolean value
print issubclass(B,A)
print isinstance(n,C)   #isinstance(obj,Class)....returns boolean value
print isinstance(m,B)
