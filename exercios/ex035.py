print('-=-' * 15)
print('ANALIZADOR DE TRIANGULOS')
print('-=-' * 15)
r1 = float(input('Primeioro segmento: '))
r2 = float(input('Segundo Segmento:'))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('esse segmmentos podem formar um triangulo')
else:
    print('esse segmentos NÂO podem form um triangulo')
