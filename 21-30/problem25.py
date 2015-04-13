# problem25.py

import math

i = 0
cnt = 2
limit = pow(10, 999)
fib = [0, 0, 0]

fib[0] = 1
fib[2] = 1

while fib[i] <= limit:
    i = (i + 1) % 3
    cnt += 1
    fib[i] = fib[(i + 1) % 3] + fib[(i + 2) % 3]

print(cnt)
