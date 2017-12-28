# input n
n = int (input ())

# input strings in a[]
a = []
for i in range (1, n + 1, +1):
    a.append (input ().strip ())

ans = []
str_smaller_count = 0
for i, j in enumerate (a):
    for k in range (0, i, +1):
        if (a[k] < a[i]):
            str_smaller_count += 1
    ans.append ((i, j, str_smaller_count))
    str_smaller_count = 0

for i in range (0, len (ans), +1):
    print (ans[i][2])
