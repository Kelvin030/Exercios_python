contador = 0
print('=' * 50)
num = (int(input('quer ver a  tabuada  de qual valor: ')))
print('=' * 50)
while True:
    if num < 0:
        break
    contador += 1
    print(f' {num} X {contador} = {num * contador}')
    if contador == 10:
        contador = contador - 10
        print('=' * 50)
        num = (int(input('quer ver a  tabuada  de qual valor: ')))
        print('=' * 50)
print('PROGRAMA DE TABUADA ENCERRADO. volte sempre!!!')
