# problem17.py

# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

s = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4, 3, 6, 6, 8, 8, 7, 7, 9, 8, 8] # 0 to 19
d = [0, 3, 6, 6, 5, 5, 5, 7, 6, 6] # 20 30 40 50 60 70 80 90
h = 7 # 100
t = 8 # 1000

z = 0
for i in range(1, 1000):
    c = int(i % 10)
    b = int(((i % 100) - c) / 10)
    a = int(((i % 1000) - (b * 10) - c) / 100)

    if a != 0:
        z += s[a] + h
        if b != 0 or c != 0:
            z += 3
    if b == 0 or b == 1:
        z += s[b * 10 + c]
    else:
        z += d[b] + s[c]

z += s[1] + t

print(z)
