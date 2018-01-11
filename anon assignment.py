#-----------anonymous fn_________

exp1=lambda a,b,c,d: (a+b)/(c-d)
exp2=lambda a,b,c,d: (a/b)/(c*d)


a=int(input("input a:"))
b=int(input("input b:"))
c=int(input("input c:"))
d=int(input("input d:"))
print "exp1 is:", exp1(a,b,c,d)
print "exp2 is:", exp2(a,b,c,d)
print "lololo"