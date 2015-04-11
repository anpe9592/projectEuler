# problem22.py

file = open("names.txt", "r")
name = []

name = sorted(file.read().replace('"', '').split(','), key = str)

l = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9, 'J':10, \
    'K':11, 'L':12, 'M':13, 'N':14, 'O':15, 'P':16, 'Q':17, 'R':18, 'S':19, \
    'T':20, 'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26}


x = len(name)
z = 0
for i in range(x):
    x2 = 0
    y = 0
    for letter in name[i]:
        x1 = l[letter]
        x2 += x1
    y = x2 * (i + 1)
    z += y

print(z)
