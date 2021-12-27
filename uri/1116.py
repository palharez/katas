n = int(input())
for i in range(n):
    nuns = input().split()
    n1, n2 = nuns
    n1 = float(n1)
    n2 = float(n2)
    if n2 == 0:
        print("divisao impossivel")
    else:
        div = n1 / n2
        print("%.1f" % div)