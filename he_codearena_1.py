# 1
# 3 2 1
# 1 2
# 2 3
# 2

t = int (input ())
for j in range (0, t, +1):
    n, f, s = (map (int, input ().strip ().split (' ')))
    a = []
    b = []
    x = []
    for i in range (0, f, +1):
        p, q = (map (int, input ().strip ().split (' ')))
        a.append (p)
        b.append (q)
    for k in range (0, s, +1):
        r = int (input ())
        x.append (r)
    print (n - len (x))
