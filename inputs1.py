import sys

n = int (sys.stdin.readline ().strip ())

n = int (input ())
n = int (sys.stdin.readline ())


a = (list (map (int, input ().strip ().split (' '))))

a = (list (map (int, sys.stdin.readline ().strip ().split (' '))))

#    print ((str (ser[k])).zfill (5), end=' ')

n, k = (map (int, input ().strip ().split (' ')))

string, k = (map (str, input ().strip ().split (' ')))

a = [int (input ()) for b in (range (n))]
arr = [int (x) for x in sys.stdin.readline ().split ()]

# initialize dictionary
dict = {}

ans = []
for i, j in enumerate (a):
    q = j % k
    ans.append ((i, j, q))
ans.sort (key=lambda x: x[0])
ans.sort (key=lambda x: x[2])
for i in ans:
    print (i[1], end=' ')


    def most_common(lst):
        return max (set (lst), key=lst.count)
