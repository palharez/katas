C = int(input())
T = input()
M = []
for linha in range(12):
    aux = []
    for coluna in range(12):
        v = float(input())
        aux.append(v)
    M.append(aux)
total = 0.0
for linha in range(12):
    total += M[linha][C]

if T == 'S':
    print("%.1f" % total)
else:
    total /= 12
    print("%.1f" % total)