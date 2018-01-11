#---file operations----------
import os
#open a file

fo=open("anku.txt","w+")

print "name of file:", fo.name
print "close status:", fo.closed
print "mode status:", fo.mode

#----write in file-----

fo.write("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

fo.close()
print "close status:", fo.closed

#---read a file--------

fo=open("anku.txt","r+")

str=fo.read(8)

print "content in file:",str
#----position------

position=fo.tell();
print "current file position:", position

#---seek(0,0)..first digit is offset after the current position
#..second digit should be 0,1,2...0 indicates cursor at the start...1 indicates from the cursor position..,,2 indicates at end
position=fo.seek(0,0) 
str=fo.read()

print "content in file:",str



#----close a file----

fo.close()
print "close status:", fo.closed
#RTYUIOP