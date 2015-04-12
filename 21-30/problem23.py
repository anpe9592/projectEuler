# problem23.py

import math

def divisors(n):
    yield 1

    largest = int(math.sqrt(n))

    if largest * largest == n:
        yield largest
    else:
        largest += 1

    for i in range(2, largest):
        if n % i == 0:
            yield i
            yield n / i

def isAbundant(n):
    if n < 12:
        return False
    return sum(divisors(n)) > n

abundants = list(x for x in range(1, 28123) if isAbundant(x))

abundantsSet = set(abundants)
def isAbundantSum(n):
    for i in abundants:
        if i > n:
            return False
        if (n - i) in abundantsSet:
            return True
    return False

sumOfNonAbundants = sum(x for x in range(1, 28123 + 1) if not isAbundantSum(x))

print(sumOfNonAbundants)
