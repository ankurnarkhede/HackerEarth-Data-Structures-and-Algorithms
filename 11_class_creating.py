#-----------creating class_---------------------

#------defining class--------

class Workshop:
    def __init__(self):
        "this is a constructor block"
        self.a= raw_input("enter your text here:")
        
    def display(self):
        print "\n the text u entered is:", self.a
        print "you just made a class and called an object"
        
#---------creating obj of class workshop

o=Workshop()

#calling the obj and thus accessing the fns and data

o.display()