#---numpy---3
import numpy as np

#1
a=np.arange(10)
print a
print a[5]
print a[-3]

#2
b=np.arange(9)#.reshape(3,3)
b.shape=(3,3) # or use the above .reshape
#print b

#3
c=np.array([[[1,2,3],[4,5,6],[7,8,9]]])
print c
print c[0,1,1]   #prints the no
print c[0,-1,-2]
print  in c