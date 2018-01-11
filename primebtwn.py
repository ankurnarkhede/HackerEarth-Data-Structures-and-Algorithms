a=10
b=20
for i in range(a,b):
    for j in range(2,i):
        if i%j==0:
            print i, "is a composite number"
            break
    else:
        print i, "is a prime number"