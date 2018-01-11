n=int(input("enter number:"))
facto=1;
c=1
if (n<0):
    print "there is no factorial of negative number"
elif n==0:
    print "factorial of 0 is 1"
else:
        while(c<=n):
            facto *= c
            c += 1
            print "factorial of no is", facto