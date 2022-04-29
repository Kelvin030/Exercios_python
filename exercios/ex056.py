media = 0
menosde20 = 0
maior = 0
hmaisvelho = 0
nome = ''
for c in range(1, 5):
    print(f'----{c}° pessoa-----')
    n = str(input('Nome: '))
    i = int(input('Idade: '))
    s = str(input('Sexo(M/F): ')).lower()
    media += i
    if c == 1 and s == 'm':
        hmaisvelho = i
        nomemaisvelho = n
    if s in 'm' and i > hmaisvelho:
        hmaisvelho = i
        nome = n
    if s == 'f' and i < 20:
        menosde20 += 1
print(f'a media das idades é {media / 4 :.0f} anos')
print(f'Ha {menosde20} mulheres com menos de 20 anos')
print(f'O homen mais velho tem {hmaisvelho} e se chama {nome}')
