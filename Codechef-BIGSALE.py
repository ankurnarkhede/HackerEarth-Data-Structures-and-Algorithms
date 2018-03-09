import sys

# test cases
t = int (sys.stdin.readline ())
for i in range (0, t, +1):
    # no of recipes...need to output one sum for each recipe
    n = int (sys.stdin.readline ())
    loss = 0
    for j in range (0, n, +1):
        price, quantity, discount = (map (int, sys.stdin.readline ().strip ().split (' ')))
        increased = price + (price * discount) / 100
        selling = increased - (increased * discount) / 100
        loss += (price - selling) * quantity
    print (loss)
