#------plot figure-------
import numpy as np
import matplotlib.pyplot as pl

fig1=pl.figure(2)  #default name of fig is  figure 1

a=np.arange(0,2*np.pi,0.1)
b=np.sin(a)
c=np.cos(a)
d=np.tan(a)
pl.title("si")

#pl.subplot(rowcolumnemement)
pl.subplot(221)
pl.plot(a,b,label="sine")

pl.subplot(222)
pl.plot(a,c,label="cosine")

pl.subplot(212)
pl.plot(a,d,label="tangent")

pl.show()