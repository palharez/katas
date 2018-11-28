n = int(input())
for i in range(n):
    entrada = input().split()
    v1, v2, v3 = entrada
    v1 = float(v1)
    v2 = float(v2)
    v3 = float(v3)
    media = ( (v1 * 0.2) + (v2 * 0.3) + (v3 * 0.5))
    print('%.1f' % media)