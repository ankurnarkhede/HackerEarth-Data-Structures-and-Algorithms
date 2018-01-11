#-----class employee----

class emp:
    def __init__(self):
        "this is emp block"
        self.name= raw_input("enter employee name:")
        self.sal=int(input("enter salary here:"))
        
        
    def display(self):
        print "***************INFO OF EMPLOYE****************"
        print "\nname of employee:",self.name
        print "salary of employee:",self.sal
        
#creating obj
a=emp()        

#calling obj
a.display()