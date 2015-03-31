# problem10.py

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

# This one will take some time

x = 2000000

z = 0
i = 1
while i < x:
    i += 1
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            z += i
            print(i)

print(z)

