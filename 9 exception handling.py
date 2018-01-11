#---------exception handling_-----------------

try:
    fh=open("mynewfile","r")   #----reading instead of writing----------------------------
    fh.write("this is test file foe exception handling")

except IOError:
    print ("Error: the system cannot find file or read data")
    
else:
    print ("heyyy!!! the cotent is written in the file successfully")
    
    
    fh.close()