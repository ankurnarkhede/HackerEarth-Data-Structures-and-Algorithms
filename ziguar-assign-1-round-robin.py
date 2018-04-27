import sys

flag = 0
try:
    fr = open ("inputfile1.txt", "r+")
    input_string = fr.read ().strip ().split (' ')
    print (input_string)

    fr1 = open ("OutputFile1.txt", "r+")
    fr2 = open ("OutputFile2.txt", "r+")
    fr3 = open ("OutputFile3.txt", "r+")

    input_string1 = fr1.read ().strip ().split (' ')
    input_string2 = fr2.read ().strip ().split (' ')
    input_string3 = fr3.read ().strip ().split (' ')

    if (input_string1 != input_string2 != input_string3):
        start = min (input_string3, input_string2, input_string1)
        flag = 1
        print ('start=', start)


    for i in range (0, len (input_string), +3):
        print (i)

        if (i == 0 and flag == 0):
            fo1 = open ("OutputFile1.txt", "w+")
            fo2 = open ("OutputFile2.txt", "w+")
            fo3 = open ("OutputFile3.txt", "w+")

            fo1.write (input_string[i] + ' ')
            fo2.write (input_string[i + 1] + ' ')
            fo3.write (input_string[i + 2] + ' ')

            fo1.close ()
            fo2.close ()
            fo3.close ()

        else:
            fo1 = open ("OutputFile1.txt", "a")
            fo2 = open ("OutputFile2.txt", "a")
            fo3 = open ("OutputFile3.txt", "a")

            try:
                fo1.write (input_string[i] + ' ')
                fo2.write (input_string[i + 1] + ' ')
                fo3.write (input_string[i + 2] + ' ')

                fo1.close ()
                fo2.close ()
                fo3.close ()

            except(IndexError):
                break


except(FileNotFoundError):
    print ('File doesnt exists')
