# https://www.hackerearth.com/practice/data-structures/hash-tables/basics-of-hash-tables/practice-problems/algorithm/pair-sums/
# 5 9
# 1 2 3 4 5

import sys
from collections import Counter


def main():
    # taking input as directed
    n, k = (map (int, sys.stdin.readline ().strip ().split (' ')))
    a = (list (map (int, sys.stdin.readline ().strip ().split (' '))))

    # counting the number of times a number occured in list into a dict
    a_counter = Counter (a)

    for number in a_counter:
        diff = k - number

        # finding if the diff is present in the dictionary, so as if added gives k
        if ((diff != number and a_counter.get (diff, 0) > 0) or (diff == number and a_counter.get (diff, 0) > 1)):
            print ("YES")
            sys.exit (0)

    print ("NO")


if __name__ == '__main__':
    main ()
