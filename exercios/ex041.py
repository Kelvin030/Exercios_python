from datetime import date
naci = int(input('digite sua idade: '))
ano = date.today().year
idade = ano - naci
if idade <= 9:
    print(f'você com {idade} anos, esta na categoria MIRIM')
elif idade <= 14:
    print(f'vcocê com {idade} anos, esta na categoria INFANTIL')
elif idade <= 19:
    print(f'você com {idade} anos, esta na categoria JÚNIOR')
elif idade <= 25:
    print(f'você com {idade} anos, esta na categoria SÊNIOR')
else:
    print(f'você com {idade} anos, esta na categoria MASTER')
