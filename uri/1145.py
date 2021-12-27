X, Y = input().split()
Y = int(Y)
X = int(X)
n = 0
for i in range(1, Y):
    n += 1
    if (n == X):
        print(i)
        n = 0
    else:
        print(i, end=" ")
print(Y)
