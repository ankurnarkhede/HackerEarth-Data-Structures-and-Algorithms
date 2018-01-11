def changeme(a):
    "appending list from fn"
    a.append([1,2,3,4,5])
    print "inside fn",a
    return a;


a=[10,20,30]
print "default list",a
changeme(a);
print "outside fn",a