import math

entrada = input()
entradaComoString = entrada.split(" ")
numeros = [int(numero) for numero in entradaComoString]

a, b, c = numeros
delta = (b ** 2) - (4 * a * c)

if delta <= 0 or a == 0:
    print('Impossivel calcular')  

else:
    R1 = (-b + math.sqrt(delta)) / (2 * a)
    R2 = (-b - math.sqrt(delta)) / (2 * a)
    print('R1 =', R1, 'R2 =', R2)