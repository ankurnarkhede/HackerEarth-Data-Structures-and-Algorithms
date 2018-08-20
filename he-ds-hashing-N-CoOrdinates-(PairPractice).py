# https://www.hackerearth.com/practice/data-structures/hash-tables/basics-of-hash-tables/practice-problems/algorithm/n-co-ordinates-pair-practice/

# 5
# 1 1
# 2 1
# 1 3
# 1 1
# 1 3


import sys
from collections import Counter


def main():
    # taking input as directed
    n = int (sys.stdin.readline ().strip ())
    arr = []

    for i in range (n):
        x, y = (map (int, sys.stdin.readline ().strip ().split (' ')))
        arr.append ((x, y))

    # counting the number of times the pair occured in list into a dict
    arr_counter = Counter (arr)

    for key in sorted (arr_counter.keys ()):
        # printing in lexicographic order
        print (key[0], key[1], arr_counter[key])


if __name__ == '__main__':
    main ()
