# problem21.py
#
# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.
#
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
#
# Evaluate the sum of all the amicable numbers under 10000.

import math

upperLimit = 10000

def sumOfFactors(num):
    sqrtOfNumber = int(math.sqrt(num))
    sum = 1

    if num == sqrtOfNumber * sqrtOfNumber:
        sum += sqrtOfNumber
        sqrtOfNumber -= 1

    for i in range(2, sqrtOfNumber):
        if num % i == 0:
            sum = sum + i + (num / i)

    return sum

sumAmicible = 0
factorsi = 0
factorsj = 0

for i in range(2, upperLimit):
    factorsi = sumOfFactors(i)
    if factorsi > i and factorsi <= upperLimit:
        factorsj = sumOfFactors(factorsi)
        if factorsj == i:
            sumAmicible += i + factorsi

print(int(sumAmicible))
