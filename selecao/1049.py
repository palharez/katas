palavraUm = input()
palavraDois = input()
palavraTres = input()

if palavraUm == 'vertebrado':
    if palavraDois == 'ave':
        if palavraTres == 'carnivoro':
            print('aguia')
        elif palavraTres == 'onivoro':
            print('pomba')
    elif palavraDois == 'mamifero':
        if palavraTres == 'onivoro':
            print('homem')
        elif palavraTres == 'herbivoro':
            print('vaca')       
elif palavraUm == 'invertebrado':
    if palavraDois == 'inseto':
        if palavraTres == 'hematofago':
            print('pulga')
        elif palavraTres == 'herbivoro':
            print('lagarta')
    elif palavraDois == 'anelideo':
        if palavraTres == 'hematofago':
            print('sanguessuga')
        elif palavraTres == 'onivoro':
            print('minhoca')