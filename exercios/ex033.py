a = int(input('digite o primeiro numero: '))
b = int(input('digite o segindo numero: '))
c = int(input('digite o terceiro numero: '))
if a< b and a < c:
    menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
print('o MENOR numero é o {}'.format(menor))
if a > b and a > c:
    maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('o MAIOR numero é o {}'.format(maior))
