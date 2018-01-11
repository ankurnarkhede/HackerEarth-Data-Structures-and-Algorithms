#-------line plot----------
import numpy as np
import matplotlib.pyplot as pl

x=[1,2,3,4,5]
y=[1,4,9,19,25]

#third attribute changes color of line...y indicates yellow...first letter
pl.plot(x,y,'y',linewidth=8)  #plots the graph x,y
pl.show()   #shows plot on screen

#----------grid-------
# shows grid in graph
#attribute acn br True or False
#color attribute changes grid color
pl.grid(True,color='b')