#---method overriding---
class Parent():
    def Pmethod(self):
        print "thid is parent method"
        
class Child(Parent):
    def Pmethod(Parent):
        print "thid is child method"
        

c=Child()


c.Pmethod()  #method overriding
#coz of same name...Child class will override its method over parent method