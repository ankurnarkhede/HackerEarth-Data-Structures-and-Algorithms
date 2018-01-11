
#-------line plot----------
import numpy as np
import matplotlib.pyplot as pl

x=[1,2,3,4,5]
y=[1,4,9,19,25]


pl.plot(x,y) 
#--imits of graph----------
pl.xlim(-1,4)
pl.ylim(-1,20)


pl.grid(True,color='b')
pl.show()   #shows plot on screen