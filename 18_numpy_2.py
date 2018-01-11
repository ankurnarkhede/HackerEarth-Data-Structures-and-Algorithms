#--------numpy with python--------
import numpy as np
#1 arange
a=np.arange(5) # reads till 5
print a
b=np.arange(3,7) # reads from 3 to 7-1
print b

#2linspace
a=np.linspace(0,20,5) #from 0 to 20...5 nos having same diff
print a

a=np.linspace(0,20,5, endpoint=False) #from 0 to 20..except 20...5 nos having same diff
print a

a=np.linspace(0,20,5, endpoint=True) #from 0 to 20...including 20...5 nos having same diff
print a