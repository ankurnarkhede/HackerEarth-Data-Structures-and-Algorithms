# hackerearth BishuAndSoldiers


n = int (input ())
a = [int (input ()) for b in (range (n))]
# print(a)
t = int (input ())
for i in range (t):
    c = 0;
    summ = 0
    poww = int (input ())
    while (c < n and a[c] <= poww):
        summ += a[c]
        c += 1
    if (c != 10000):
        print (c * 100, summ * 100)
    else:
        print (c, summ)
