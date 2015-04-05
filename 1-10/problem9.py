# problem9.py

# A Pythagorean triplet is a set of three natural numbers,
#  a < b < c, for which, a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

a = 0
b = 0
c = 0
z = 1000

x = int(z / 3)
y = int(z / 2)
for a in range(x):
    b = a + 1
    for b in range(y):
        c = z - a - b
        if a*a + b*b == c*c:
            print("a =", a, "b =", b, "c =", c)
            print("abc =", a * b * c)
