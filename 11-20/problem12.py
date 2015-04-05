# problem12.py

import math

x = 0
z = 0
n = 1

i = True
while i != False:
    z = n * (n + 1) / 2
    x = 2
    
    y = int(math.sqrt(z))
    for k in range(2, y):
        if z % k == 0:
            x += 2
        if x == 500:
            i = False

    n += 1

print(z)
