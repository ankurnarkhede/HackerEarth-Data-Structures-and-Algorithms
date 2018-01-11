
#-------line plot----------
import numpy as np
import matplotlib.pyplot as pl

x=[1,2,3,4,5]
y=[1,4,9,19,25]


pl.plot(x,y,label="plot 1") 
pl.legend()
pl.xlabel("time")
pl.ylabel("distance")


pl.grid(True,color='b')
pl.show()   #shows plot on screen