#------------numpy----5

import numpy as np

#1
a=np.array([[[1,2,3],[4,5,6],[7,8,9]]], float)
b=np.array([[[3,4,5],[4,5,6],[7,8,9]]], float)
c=np.concatenate((a,b))
print "c=",c
d=np.concatenate((a,b), axis=0)
print "d=",d
e=np.concatenate((a,b), axis=1)
print "e=",e