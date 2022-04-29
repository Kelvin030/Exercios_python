n = str(input('digite seu sexo[F/M]: ')).lower().strip()[0]
while n not in 'mf':
    n = str(input('sexo invalido, tente novamente: ')).lower().strip()[0]
print('FIM')
