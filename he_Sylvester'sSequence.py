num = 6

arr = []
prod = 1

arr.append (2)
print (arr)
for i in range (0, num - 1, +1):
    term = 0
    prod = 1
    print ('i================', i)
    for j in range (0, i + 1, +1):
        print ('arr[j]=', arr[j])
        prod *= arr[j]
        print ('prod=', prod)
    term = prod + 1
    print ('term=', term)
    arr.append (term)

print (arr)
