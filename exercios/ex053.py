frase = str(input('digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
invertido = ''
for letra in range(len(junto)-1, -1,-1):
    invertido += junto[letra]
if junto == invertido:
    print(f' a frase {frase}, é uma Palíndroma')
    print(f'o inverso de {frase} é {invertido}')
else:
    print(f'a frase {frase} não é Palíndroma')
    print(invertido)
