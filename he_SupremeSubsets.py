import itertools

comb1 = []
low = 999999999
index = 0
# imput n,m
n, m = (map (int, input ().strip ().split (' ')))
# print('n=',n,'m=',m)
# cardinality=abs(n-m)
cardinality = 2
print (cardinality)

a = (list (map (int, input ().strip ().split (' '))))
comb = list (itertools.permutations (a, 2))
# print('comb=',comb)

for i in range (0, len (comb), +1):
    # print('checking',comb[i])
    if (abs (comb[i][0] - comb[i][1]) % m == 0):
        comb1.append (comb[i])

# print('comb1=',comb1)

for i in range (0, len (comb1), +1):
    # print('checking',comb1[i])
    if (sum (comb1[i]) < low):
        low = sum (comb1[i])
        index = i

# print('index=',index)
print (comb1[index][0], ' ', comb1[index][1], sep='')
