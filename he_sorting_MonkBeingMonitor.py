for i in range (0, int (input ()), +1):
    n = int (input ())
    # print ('No of students:'+ str(n))
    a = (list (map (int, input ().strip ().split (' '))))
    # print ('heights:'+ str(a))

    print (len (a) - a.count (max (a)) - a.count ((min (a))))
