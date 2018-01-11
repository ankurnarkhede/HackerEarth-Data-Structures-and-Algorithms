#-----------keyword arguments.....printing n times-----------
def keyword(name, n=1): #default value is 1
    "prints name for n times"
    for i in range(0,n):
        print "my name is",name
    return
    

#--calling fn
keyword("lol")

keyword("lol00", 4)