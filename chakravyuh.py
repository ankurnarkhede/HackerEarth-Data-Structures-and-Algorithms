n=int(input("Enter the size of matrix:"))
r=n
c=n
t=1
x=0
y=0
a=[[0 for i in range (n)]for j in range (n)]

while (x<=r and y<=c):
    for i in range(y,c,+1):
        a[y][i]=t
        t+=1
    x+=1

    for i in range(x,r,+1):
        a[i][c-1]=t
        t+=1  
    c-=1
   
    for i in range(c,y,-1):
        a[c][i-1]=t
        t+=1
    r-=1
    

    for i in range(r,x,-1):
        a[i-1][y]=t
        t+=1
    y+=1
    

for i in range(0,n):
    for j in range(0,n):
        print ("   ",str(a[i][j]).zfill(3), end='')
    print()