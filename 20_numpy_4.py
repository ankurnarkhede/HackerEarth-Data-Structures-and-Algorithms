#------------numpy----4

import numpy as np

#1
a=np.array([1,2,3])
print "original a:",a
print a.tolist()
b=a
c=a.copy() #separate copy..not affeced by changing a,b
print c
b[0]=0
#print c
print "b:", b
print "a:",b