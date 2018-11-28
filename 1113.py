i = 1
while i != 0:
    a, b = input().split()
    a = int(a)
    b = int(b)

    if a > b:
        print('Decrescente')
    elif a == b:
        break
    else:
        print('Crescente')