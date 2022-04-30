from ast import alias


aluno = {}
aluno['nome'] = str(input("Nome: "))
aluno['nota'] = float(input('Nota Medía: '))
print(f"O nome do aluno é {aluno['nome']}")
print(f"A nota é {aluno['nota']}")
if aluno['nota'] >= 7:
    print("O aluno foi aprovado!!!")
else:
    print("O aluno foi reprovado!!!")
