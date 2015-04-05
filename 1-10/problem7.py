# problem7.py

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

i = 1
z = 1
while i < 10002:
    z += 1
    if z > 1:
        for j in range(2, z):
            if z % j == 0:
                break
        else:
            i += 1

print(z)
