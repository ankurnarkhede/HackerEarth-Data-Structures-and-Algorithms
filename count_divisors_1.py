x=int(input())
y=int(input())
z=int(input())
count=0
for i in range(x,y+1,+1):
    if(i%z==0):
        count+=1
print (count)