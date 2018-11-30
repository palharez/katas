x = int(input())
aux = 0
n = 1
while aux == 0:
    z = int(input())
    if z > x:
        aux = 1
y = x
while x <= z:
    n += 1
    y += 1
    x += y

print(n)
