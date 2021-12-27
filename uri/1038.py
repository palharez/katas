comidas = [4, 4.50, 5, 2 , 1.50]
entrada = input()
entradaComoString = entrada.split(" ")
numeros = [int(numero) for numero in entradaComoString]
num, quant = numeros
total = 0

for i in range(quant):
    total += comidas[num -1]

print("Total: R$ %.2f" % total)