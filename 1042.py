entrada = input().split()
n1, n2, n3 = entrada

n1 = int(n1)
n2 = int(n2)
n3 = int(n3)
maior = 0
menor = 0
meio = 0

if n1 > n2 and n1 > n3:
    maior = n1
    if n2 >= n3:        
        meio = n2
        menor = n3
    else:        
        meio = n3
        menor = n2
elif n2 > n1 and n2 > n3:
    maior = n2
    if n1 >= n3:        
        meio = n1
        menor = n3
    else:        
        meio = n3
        menor = n1
elif n3 > n1 and n3 > n2:
    maior = n3
    if n1 >= n2:        
        meio = n1
        menor = n2
    else:        
        meio = n2
        menor = n1

print(menor)
print(meio)
print(maior)
print()
print(n1)
print(n2)
print(n3)