n = int(input())

for i in range(n):
    c = float(input())
    dias = 0

    while c > 1:
        c /= 2
        dias += 1

    print(str(dias) + " dias")