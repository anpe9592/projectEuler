# problem24.py

perm = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def swap(i, j):
    k = perm[i]
    perm[i] = perm[j]
    perm[j] = k

count = 1
numPerm = 1000000

while count < numPerm:
    N = len(perm)
    i = N - 1

    while perm[i - 1] >= perm[i]:
        i = i - 1

    j = N
    while perm[j - 1] <= perm[i - 1]:
        j = j - 1

    swap(i - 1, j - 1)

    i += 1
    j = N

    while i < j:
        swap(i - 1, j - 1)
        i += 1
        j -= 1
    count += 1

permNum = ""
for k in range(len(perm)):
    permNum = permNum + str(perm[k])

print(permNum)
