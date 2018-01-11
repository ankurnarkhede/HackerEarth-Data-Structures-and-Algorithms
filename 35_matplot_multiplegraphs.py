
#-------plot 2 graphs simpltaneously----------
import numpy as np
import matplotlib.pyplot as pl

t=np.arange(0,2*np.pi,0.1)   #----diff of 0.1
x=np.sin(t)
y=np.cos(t)

pl.plot(t,x,'r*') 
pl.plot(t,y,'b*')

pl.grid(True,color='b')
pl.show()   #shows plot on screen