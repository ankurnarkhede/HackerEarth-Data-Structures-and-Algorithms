import sys
from collections import deque

q = int (sys.stdin.readline ())
monk_queue = deque ([])
x, y = 0, 0

for i in range (0, q, +1):
    print ('=========================\nq=', monk_queue)
    ip = (sys.stdin.readline ().strip ().split (' '))
    if (len (ip) == 3):
        char, x, y = ip[0], ip[1], ip[2]
    elif (len (ip) == 1):
        char = ip[0]

    print ('input=', char, x, y)

    if (char == 'E'):
        flag_e = 0
        x, y = int (x), int (y)
        for j in range (len (monk_queue) - 1, 0, -1):
            # if he found his friend
            print ('to check=', monk_queue[j][0])
            if (monk_queue[j][0] == x):
                monk_queue.insert (monk_queue[j + 1], [x, y])
                flag_e = 1
                print ('found frnd')
                break

        if (flag_e == 0):
            monk_queue.append ([x, y])
            print ('frnd not found')


    elif (char == 'D'):
        monk_queue.popleft ()

print (monk_queue)


