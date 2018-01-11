#-----class employee,,,attributes----

class emp:
    def __init__(self):
        "this is emp block"
        self.name= raw_input("enter employee name:")
        self.sal=int(input("enter salary here:"))
        
        
    def display(self):
        print "***************INFO OF EMPLOYE****************"
        print "\nname of employee:",self.name
        print "salary of employee:",self.sal,"age=",self.age
        
#creating obj
a=emp() 
emp.age=20       
b=hasattr(emp,'age')
print b
n=getattr(emp,'age')
print n

#calling obj
a.display()