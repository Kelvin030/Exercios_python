from math import radians, sin, cos, tan
angulo = float(input('digite o Ângulo: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print(f'o angulo de {angulo} tem o SENO de {seno :.2f}')
print(f'o angulo de {angulo} tem o COSSENO de {cosseno :.2f}')
print(f'o angulo de {angulo} tem a TANGENTE de {tangente :.2f}')
