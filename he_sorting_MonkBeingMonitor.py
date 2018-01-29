# choose 2 students having heights h1 and h2 respectively,
# such that h1>h2 and difference between the
#  number of students having height h1 and number of students having height h2 is maximum.

import sys

for i in range (0, int (sys.stdin.readline ()), +1):
    n = int (sys.stdin.readline ())
    a = (list (map (int, sys.stdin.readline ().strip ().split (' '))))

    # logic s

    set_a = set (a)
    diff = a.count (max (set_a, key=a.count)) - a.count (min (set_a, key=a.count))

    # logic e

    print (diff) if diff > 0 else print (-1)

