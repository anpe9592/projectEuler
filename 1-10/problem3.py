# problem3.py

# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

number = 600851475143

divider = 2

while number != 1:
    if number % divider == 0:
        number = number / divider
        print(divider)
    else:
        divider += 1
