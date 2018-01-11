#------plot piechart-------
import numpy as np
import matplotlib.pyplot as pl

label='cse','it','mech','extc'
values=[120,60,50,89]
colors=['yellow','blue','green','red']
explode=(0.1,0,0,0) #...separates first element by 0.1 unit

pl.pie(values,labels=label, colors=colors,explode=explode,autopct='1%.2f%%',shadow=True,startangle=90)
#put names of variales into which labels colors explode is entered
#enter shadow=True or False

pl.axis('equal') #makes both axes equal...perfect circle pie chart
pl.show()