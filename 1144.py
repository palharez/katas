N = int(input())
aux = 0
for i in range(N):
    aux += 1
    for x in range(0, 3):
        if (x == 0):
            print(aux, end=" ")
        elif (x == 1):
            print(aux ** 2, end=" ")
        else:
            print(aux ** 3)
    for x in range(0, 3):
        if (x == 0):
            print(aux, end=" ")
        elif (x == 1):
            print((aux ** 2) + 1, end=" ")
        else:
            print((aux ** 3) + 1)
