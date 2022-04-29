numeros = ('zero','um', 'dois','tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze',
           'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    resposta = int(input('digitem um numero entre 0 e 20: '))
    if 0 <= resposta <= 20:
        break
    print('tente novamente. ', end=' ')
print(numeros[resposta])

