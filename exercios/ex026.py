frase = str(input('digite uma frase: ')).strip().lower()
print('a letra A aparece {} vezes.'.format(frase.count('a')))
print('a letra A aparece primeiro na posição {}'.format(frase.find('a') + 1))
print('a letra A aparece pela ultima vez na posição {}'.format(frase.rfind('a') + 1))