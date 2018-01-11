#------inheritance------

class Parent():
    def __init__(self):
        print"i m parent constructor"
        
    def block(self):
        print "i m block in parent"
        
a=Parent()
a.block   
#  a.childmet()
        
class Child(Parent):
    def __init__(self):
        print "i m child"
        
    def childmet(Parent):
        print "i m child method"
        
t=Child()
t.block()
t.childmet()