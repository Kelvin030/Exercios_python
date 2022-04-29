A = int(input('Primeiro valor: '))
B = int(input('Segundo valor: '))
if A > B:
    print('O \033[32mPRIMEIRO\033[m valor è MAIOR!')
elif B > A:
    print('O \033[32mSEGUNDO\033[m valor é MAIOR')
else:
    print('Os \033[32mDOIS\033[m valore são IGUAIS')
