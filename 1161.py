def fatorial (n):
    if n < 0:
        return 0
    i = fat = 1
    while i <= n:
        fat = fat * i
        i = i + 1
    return fat

x = 0
for x in range(0, 3):
    a, b = input().split()
    a = int(a)
    b = int(b)
    s = fatorial(a) + fatorial(b)
    print(s)