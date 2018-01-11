
import sys

l=[]
r=[]


n,q=3,3
l.extend([11,31,51])
r.extend([20,40,60])

print("l=",l)
print("r=",r)


# n, q = (map(int, input ().strip ().split (' ')))
# for i in range(0,n,+1):
#     a,b = (map (int, input ().strip ().split (' ')))
#     l.append(a)
#     r.append(b)

for j in range(0,q,+1):
    x=int(input())
    small = 0

    for i in range (sys.maxsize ** 10):
        print("checking for ",x," for ",i,"th time")
        print("l[i]=",l[i]," r[i]=",r[i])
        print('small=',small)
        if( (l[i]-small+x-1) < (r[i]) ):
            small=l[i]-small+x-1
            print("---------small index=",small)
            # print(small)
            break
        else:
            small =small+ (r[i]-l[i]+1)