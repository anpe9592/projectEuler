# problem67.py

r = [ ]
file = open("problem67.txt", "r")
for x in file:
    r.append([int(i) for i in x.split(" ")])

for i, j in [(i, j) for i in range(len(r) -2, -1, -1) for j in range(i + 1)]:
    r[i][j] += max([r[i + 1][j], r[i + 1][j + 1]])

print(r[0][0])
