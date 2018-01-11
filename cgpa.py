#--cgpa program--------------
def grade(gr):
    "to return value of grade"
    if(gr == "A+"):  return 10;
    elif (gr == "A"):  return 9;
    elif (gr == "B+"):  return 8;
    elif (gr == "B"):  return 7;
    elif (gr == "C+"):  return 6;
    elif (gr == "C"):  return 5;
    elif (gr == "D"):  return 4;
    elif (gr == "F"):  return 0;

#main-----------------

print '##########enter grades in upper case############'

em1=raw_input("enter em1 grade:")
emth=raw_input("enter emth grade:")
empr=raw_input("enter empr grade:")
eeeth=raw_input("enter eeeth grade:")
eeepr=raw_input("enter eeepr grade:")
ecth=raw_input("enter ecth grade:")
ecpr=raw_input("enter ecpr grade:")

sga = (( 5.0*grade(em1) + 4.0*grade(emth) + 1.0*grade(empr) + 4.0*grade(eeeth) + 1.0*grade(eeepr) + 4.0*grade(ecth) + 1.0*grade(ecpr)) / 20.0)
print 'ur sga is', sga
