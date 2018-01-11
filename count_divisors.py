n=raw_input()
a,b,c=n.split(" ")
x=int(a)
y=int(b)
z=int(c)
count=0
for i in range(x,y+1,+1):
    if(i%z==0):
        count+=1
print (count)