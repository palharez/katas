m1 = None
m2 = None
x = 0

while x < 2:
    n = float(input())
    if n < 0 or n > 10:
        print("nota invalida")
    else:
        if x == 0:
            m1 = n
        else:
            m2 = n
        x += 1

media = (m1 + m2) / 2
print("media = %.2f" % media)