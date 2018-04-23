import sys

try:
    fr = open ("inputfile1.txt", "r+")
    input_string = fr.read ().strip ().split (' ')

    for i in range (0, len (input_string), +3):




except(FileNotFoundError):
    print ('File doesnt exixts')
