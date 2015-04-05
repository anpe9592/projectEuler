# problem5.py

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

x = 1
i = 0

while i < 20:

    i += 1
    if x % i != 0:
        x += 1
        i = 0

print(x)
