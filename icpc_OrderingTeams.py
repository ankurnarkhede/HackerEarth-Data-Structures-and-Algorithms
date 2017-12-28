def if_greater(a, b):
    lol = False
    for j in range (0, 2, +1):
        if (a[j] >= b[j]):
            lol = True
        if ((sum (a) > sum (b)) and lol != False):
            return True
        return False


def if_smaller(a, b):
    lol = False
    for j in range (0, 2, +1):
        if (a[j] <= b[j]):
            lol = True
        if ((sum (a) < sum (b)) and lol != False):
            return True
        return False


flag = False
n = int (input ())
for i in range (n):
    a = (list (map (int, input ().strip ().split (' '))))
    b = (list (map (int, input ().strip ().split (' '))))
    c = (list (map (int, input ().strip ().split (' '))))

    # print ('a=', a)
    # print ('b=', b)
    # print ('c=', c)

    for j in range (0, 2, +1):
        # print('j=',j)
        flag = False

        if (if_greater (a, b) and if_greater (a, c)):
            if (if_greater (b, c)):
                print ('yes')
                flag = True
                break
            elif (if_greater (c, b)):
                print ('yes')
                flag = True
                break

        if (if_greater (c, b) and if_greater (c, a)):
            if (if_greater (b, a)):
                print ('yes')
                flag = True
                break
            elif (if_greater (b, a)):
                print ('yes')
                flag = True
                break

        if (if_greater (b, c) and if_greater (b, a)):
            if (if_greater (c, a)):
                print ('yes')
                flag = True
                break
            elif (if_greater (c, a)):
                print ('yes')
                flag = True
                break

        # smaller

        if (if_smaller (a, b) and if_smaller (a, c)):
            if (if_smaller (b, c)):
                print ('yes')
                flag = True
                break
            elif (if_smaller (c, b)):
                print ('yes')
                flag = True
                break

        if (if_smaller (c, b) and if_smaller (c, a)):
            if (if_smaller (b, a)):
                print ('yes')
                flag = True
                break
            elif (if_smaller (b, a)):
                print ('yes')
                flag = True
                break

        if (if_smaller (b, c) and if_smaller (b, a)):
            if (if_smaller (c, a)):
                print ('yes')
                flag = True
                break
            elif (if_greater (c, a)):
                print ('yes')
                flag = True
                break

    if (flag != True):
        print ('no')
