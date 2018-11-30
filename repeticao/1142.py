N = int(input())
aux = 0
for i in range(N):
    for x in range(0, 4):
        aux += 1
        if (x == 3):
            print("PUM")
        else:
            print(aux, end=" ")
