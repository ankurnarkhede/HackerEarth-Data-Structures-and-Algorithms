for i in range (int (input ())):
    n = int (input ());
    p = (list (map (int, input ().strip ().split (' '))))
    p1 = sorted (p)
    print ("sorted:", p1)

    for i in range (0, n + 1, +1):
        c = p1.count (p1[i])
        if (p1.count (p1[i]) == 1):
            print (p1[i])
            break
        else:
            continue
