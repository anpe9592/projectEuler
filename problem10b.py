# problem10b.py

n = 2000000

x = [True] * n

def mark(x, z):
    for i in range(z+z, len(x), z):
        x[i] = False

for j in range(2, int(len(x) ** 0.5) + 1):
    if x[j]:
        mark(x, j)

sum = 0
for i in range(2, len(x)):
    if x[i]:
        sum += i

print(sum)
