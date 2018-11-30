x = []
for i in range(10):
    n = int(input())
    x.append(n)

for i in range(len(x)):
    if x[i] <= 0:
        x[i] = 1

for i in range(len(x)):
    print("X[" + str(i) + "] = %d" % x[i])
