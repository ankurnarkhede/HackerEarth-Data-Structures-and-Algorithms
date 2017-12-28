# hackerearth charsi in love


def charsi_in_love(n):
    num = {}
    for i in range (0, 10 ** 5, 1):
        num[(i * (i + 1) // 2)] = 1

    for i in sorted (list (num.keys ())):
        if (n - i in num):
            return 'YES'
    return 'NO'


n = int (input ())
result = charsi_in_love (n)
print (result)
