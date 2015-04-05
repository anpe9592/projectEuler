# problem14.py

mil = 1000001
z = 0
u = 0
for x in range(mil):
    print("start: ", x)
    i = x
    y = 0
    while x != 1:
        if (x % 2) == 1 or x == 0:
            x = int(3 * x + 1)
        else:
            x = int(x / 2)

        print(x)

        y += 1

    if z < y:
        z = y
        u = i

print("Count: ", z)
print("Number: ", u)
