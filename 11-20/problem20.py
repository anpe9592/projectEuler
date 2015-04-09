# problem20.py
#
# n! means n × (n − 1) × ... × 3 × 2 × 1
#
# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
#
# Find the sum of the digits in the number 100!

z = 1

x = 100
while x > 0:
    z = z * x
    x -= 1

y = [int(i) for i in str(z)]
print(sum(y))
