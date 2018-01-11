def changeme(a):
    "overwrite list from fn"
    a=[1,2,3,4,5]
    print "inside fn",a
    return a;


a=[10,20,30]
print "default list",a
changeme(a);
print "outside fn",a