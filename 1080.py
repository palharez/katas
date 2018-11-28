maior = int(input())
pos = 0

for i in range(1, 100):
    n = int(input())
    if n > maior:
        maior = n
        pos = i

print(maior)
print(pos + 1)