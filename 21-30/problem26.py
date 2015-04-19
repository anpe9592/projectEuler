# problem26.py

z = 0
u = 0

i = 1000
while i > 0:
    if z >= i:
        break

    x = [0]*i
    y = 1
    j = 0

    while x[y] == 0 and y != 0:
        x[y] = j
        y *= 10
        y %= i
        j += 1

    if j - x[y] > z:
        u = i
        z = j - x[y]

    i -= 1

print(z)
print(u)
