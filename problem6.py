# problem6.py

x = 0
z = 0
for i in range(101):
    x = i * i
    z += x

u = 0
for j in range(101):
    u += j

u = u * u


z = u - z

print(z)
