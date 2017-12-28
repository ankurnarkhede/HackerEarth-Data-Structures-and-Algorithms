# No two consecutive characters are the same.
# No two consecutive characters are in the following vowel set: a, e, i, o, u, y. Note that we consider y to be a vowel in this challenge.

v = ['a', 'e', 'i', 'o', 'u', 'y']
flag = 0
w = input ().strip ()
print ("word=", w)
len_w = len (w)
print ("len_w=", len_w)

for i in range (0, len_w - 1, 1):
    if ((w[i] in v) and (w[i + 1] in v)):
        print ("not beautiful")
        flag = 0
        break
    flag = 1
    print ("flag1")

if (flag == 1):
    print ("Yes")
elif (flag == 0):
    print ("No")
