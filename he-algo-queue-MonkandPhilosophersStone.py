import sys

n = int (sys.stdin.readline ().strip ())
worth = (list (map (int, sys.stdin.readline ().strip ().split (' '))))
q, x = (map (int, sys.stdin.readline ().strip ().split (' ')))

for i in range (0, q, +1):
    query = (sys.stdin.readline ().strip ())
