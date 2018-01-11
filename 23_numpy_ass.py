#------------numpy----6

import numpy as np
#1
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
b=a.copy()
o=a.copy()# matrix of odd
e=a.copy()# matrix of even

for i in range(0,3):
    for j in range(0,3):
        if b[i][j]%2==0:
            o[i][j]=0
            e[i][j]=b[i][j]
        else:
            o[i][j]=b[i][j]
            e[i][j]=0
            
            
#print "b=",b
#print 'odd=',o
#print 'even=',e

for i in range(0,3):
    for j in range(0,3):
        print b[i][j],
    print ''