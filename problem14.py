# problem14.py

x = 13

z = 0

while x != 1:
    if (x % 2) == 1 or x == 0:
        x = int(3 * x + 1)
    else:
        x = int(x / 2)

    print(x)

    z += 1
        
print(z)
