entrada = input()
entradaComoString = entrada.split(" ")
numeros = [float(numero) for numero in entradaComoString]

N1, N2, N3, N4 = numeros
N1 = (N1 * 2) / 10
N2 = (N2 * 3) / 10
N3 = (N3 * 4) / 10
N4 = (N4 * 1) / 10
media = N1 + N2 + N3 + N4


print('Media: %.1f' % media)
if media >= 7.0:
    print('Aluno aprovado.')
elif media < 5.0:
    print('Aluno reprovado.')
else:
    print('Aluno em exame.')
    exame = float(input())    
    mediaFinal = (media + exame) / 2
    if mediaFinal >= 5.0:
        print('Nota do exame: %.1f' % exame)
        print('Aluno aprovado.')
    else:
        print('Nota do exame: %.1f' % exame)
        print('Aluno reprovado.')
    print('Media final: %.1f' % mediaFinal)