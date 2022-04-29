n = int(input('Digite o número para a conversão: '))
print('''Escolha a forma de Conversão:
[ 1 ] converter para BINARIO')
[ 2 ] converter para OCTAL')
[ 3 ] coverter para HEXADECIMAL''')
r = int(input('sua escolha: '))
if r == 1:
    print(f'{n} é ingual a {bin(n)[2:]} em BINARIO')
elif r == 2:
    print(f'{n} é ingual a {oct(n)[2:]} em OCTAL')
elif r == 3:
    print(f'{n} é ingual a {hex(n)[2:]} em HEXADECIMAL')
else:
    print(f'não á nem uma função com {r} reinicie o programa')