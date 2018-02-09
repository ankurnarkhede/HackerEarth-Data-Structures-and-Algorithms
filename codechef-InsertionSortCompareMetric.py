import sys


def compare(a, b, cmp_count):
    cmp_count += 1
    if a > b:
        return 1, cmp_count
    else:
        return -1, cmp_count


def swap(a, x, y, sw):
    a[x], a[y] = a[y], a[x]
    sw += 1
    return sw


def InsertionSort(A):
    cmp_count = 0
    swap_count = 0
    for i in range (1, len (A) + 1, +1):
        j = i - 1
        while j > 0:
            res, cmp_count = compare (A[j - 1], A[j], cmp_count)
            if res > 0:
                swap_count = swap (A, j, j - 1, swap_count)
                j = j - 1
            else:
                break
    print (cmp_count - swap_count)


t = int (sys.stdin.readline ().strip ())

for i in range (0, t, +1):
    n = int (sys.stdin.readline ().strip ())
    a = (list (map (int, sys.stdin.readline ().strip ().split (' '))))
    InsertionSort (a)
