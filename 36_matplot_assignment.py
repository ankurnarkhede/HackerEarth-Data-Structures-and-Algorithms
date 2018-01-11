#-----------matplot assignment------

import numpy as np
import matplotlib.pyplot as pl

x=[0,1,2,3,4,5,7,8,9,10,11]
y1=[0,1,44,9,15,25,22,12,32,11,7]
y2=[0,10,4,10,25,15,2,1,32,3,17]

pl.plot(x,y1,'g',linewidth=6,label="plot 1")
pl.plot(x,y2,'--s',label="plot 2")
pl.xlabel("x-axis")
pl.ylabel("y-axis")
pl.title("ANKUR", fontsize=50)
pl.legend()

pl.grid(True,color='b')
pl.show()