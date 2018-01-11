#------------numpy----5

import numpy as np

#1
a=np.array([[1,2,3],[4,5,6]])
print ('a=',a)

#2
b=np.identity(4) #--identity matrix
print ('b=',b)

#3
c=np.eye(4,k=1,dtype=float)#shifting the 1's in identity matrix
print ('c=',c)

#4
d=np.eye(4,k=-3,dtype=float)
print ('d=',d)