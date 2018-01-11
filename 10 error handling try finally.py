#-----------error handling----try finally

try:
    fh=open("mynewfile.txt","w")
    fh.write("sample file 1 for demo of error handling")
    print ("sample file created")
    
finally:
    print ("this portion will be executed \n even if theres no error")
    
    