#--------pandas--------------
#----------coding utf-8----------

import pandas as pd
m=pd.Series(list('abcdef'))
n=pd.Series([1,2,3,4,5,6])

s=pd.Series([1,2,3,4],index=['f','a','c','e'])

print s['a']
print s[['a','e']]
s2=pd.Series(range(4),index=list('abab'))
print s2['a']
print s2['a'][2]

#print s[s>2]
#print s>2


print s*2
s2=pd.Series([1,2,3],index=list('cba'))
print s*s2