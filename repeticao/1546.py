entrada = input()
n = int(entrada)

while 1:
    if n == 0:
        print("vai ter copa")
    else:
        print("vai ter duas")
    entrada = input()
    if entrada == 'EOF':
        break
    else:
        n = int(entrada)
