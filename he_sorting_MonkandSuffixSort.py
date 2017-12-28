# taking input string and k
str, k = (map (str, input ().strip ().split (' ')))

arr = []
for i, j in enumerate (str, 1):
    arr.append ((i, str[i - 1:]))

arr.sort (key=lambda x: x[1])

print (arr[int (k) - 1][1])
