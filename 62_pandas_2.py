#--------pandas--------------
#----------coding utf-8----------

import pandas as pd
d=[0,1,2,3,4,5,6,7,8,9]
df=pd.DataFrame(d)
print df


#add a column
df['newcol']=5
print ''
print df

#modify column
df['newcol']=df['newcol']+1
print df

#delete column
