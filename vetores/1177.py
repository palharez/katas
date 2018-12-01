n = []
t = int(input())
x = 0
i = 0
while i < 1000:
    if x == t:
        x = 0
    n.append(x)
    print("N [%d] = %d" % (i, n[i]))
    x += 1
    i += 1
