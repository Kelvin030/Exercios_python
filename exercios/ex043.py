a = float(input('digite su altura: '))
p = float(input('digite seu peço: '))
r = p / (a * a)
print(f'sue IMC é de {r :.1f}')
if r < 18.5:
    print('voçe esta ABAIXO do peso')
elif 18.5 >= r <= 25:
    print('Você esta no peso IDEAL')
elif 25 > r <= 30:
    print('você esta com SOBREPESO')
elif 30 > r <= 40:
    print('você esta com OBSIDADE')
else:
    print('você esta com OBSIDADE MÓRBIDA')
