# problem15.py

size = 20
grid = [[0 for x in range(size)] for x in range(size)]

z = 2
for x in range(size):
    grid[0][x] = z
    grid[x][0] = z
    z += 1

n = size * 2
u = 0
i = 1
j = 1
while u < n:
    for x in range(i, size):
        grid[j][x] = grid[i][x-1] + grid[x][i-1]
        grid[x][j] = grid[i][x-1] + grid[x][i-1]

    u += 1
    i += 1
    j += 1    

for x in range(size):
    print(grid[x])
