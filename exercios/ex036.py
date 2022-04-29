casa = float(input('digite o valor da casa:R$'))
salario = float(input('seu salario:R$'))
ano = int(input('em quantos anos você que financiar: '))
prestação =casa / (ano * 12)
s2 = (salario * 30) / 100
if s2 >= prestação:
    print('O emprestimo pode ser \033[32mCONCEDIDO\033[m!!!')
else:
    print('O empréstimo \033[31mNÂO\033[m pode ser concedido!')
print('as Prestaçãoes ficaram emR${:.2f}'.format(prestação))