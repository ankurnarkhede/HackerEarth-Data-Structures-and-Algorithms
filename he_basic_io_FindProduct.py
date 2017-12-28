n = int (input ())
a = input ()
t = a.split (' ')
p = 1
for i in range (0, len (t)):
    p = p * int (t[i])
t1 = p % (10 ** 9 + 7)
print (t1)
