#-----------global local variables---------------------------------------------
result = 0

def sum(a,b):
    result=a+b
    print "inside fn..result=",result
    return result;
    

#------main-------------------------------------------------------------------

sum(10,5)
print "outside fn..result=",result