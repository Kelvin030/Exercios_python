'''c1 = float(input('digite o valor do cateto oposto: '))
c2 = float(input('digite o valor do cateto adjecente:'))
r = (c1**2 + c2**2) ** (1/2)
print(f'a hipotenusa vai medir {r}')'''
from math import hypot
c1 = float(input('digite o cateto oposto: '))
c2 = float(input('digite o cateto adjacente: '))
h = hypot(c1, c2)
print(f'A hipotenusa é {h}')
