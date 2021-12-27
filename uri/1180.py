N = int(input())

lista = input().split()
menor = lista[0]

for i in range(len(lista)):
    lista[i] = int(lista[i])

menor = lista[0]

for i in range(len(lista)):
    if lista[i] < menor:
        menor = lista[i]
    
print("Menor valor: %d" % menor)
print("Posicao: %d" % lista.index(menor))