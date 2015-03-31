#problem2.py

x = 1
y = 0
z = 0
sum = 0

four = 4000000

while z < four:
    z = x + y
    x = y
    y = z
    if z % 2 == 0:
        sum = sum + z

print(sum)

