from datetime import date
nac = int(input('digite sua data de nacimento: '))
data = date.today().year
idade = data - nac
if idade == 18:
    print('voce tem que se alistar IMEDIATAMENTE!!!')
elif idade < 18:
    print(f'falta {18 - idade} anos para você se alistar')
elif idade > 18:
    print(f'você deveria ter se alistado {idade - 18} anos atrás')
