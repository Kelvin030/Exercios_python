n1 = float(input('Promeira Nota: '))
n2 = float(input('Segunda Nota: '))
m = (n1 + n2) / 2
if m < 5:
    print(f'A media foi {m :.1f} o aluno foi \033[31mREPROVADO')
elif m < 6.9:
    print(f'A media foi de {m :.1f} o aluno esta de \033[31mRECUPEÇÂO')
else:
    print(f'A media foi de {m :.1f} o aluno foi \033[32mAPROVADO')
