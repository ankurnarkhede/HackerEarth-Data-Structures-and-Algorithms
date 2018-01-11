#-------line plot----------
import numpy as np
import matplotlib.pyplot as pl

x=[1,2,3,4,5]
y=[1,4,9,19,25]


pl.bar(x,y)  #plots bar
pl.show()   #shows bar on screen


pl.grid(True,color='b')