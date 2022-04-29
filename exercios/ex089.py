geral = []
aluno = []
nota = []

# Coleta dos Dados

while True:
    aluno.append(str(input("Digite o nome do aluno: ")))
    for c in range(0, 2):
        nota.append(float(input(f"Digite a {c+1}° nota: ")))   
    aluno.append(nota.copy())
    geral.append(aluno.copy())
    nota.clear()
    aluno.clear()   
    resp = str(input("Deseja continuar[S/N]:")).upper()
    print("-=" * 30)
    if resp == "N":
        break

# Media das notas

for a in geral:
    media = (a[1][0] + a[1][1]) / 2
    print(f"O aluno(a){a[0]}, tirou {media} na media")
    media = 0
print("-=" * 30)

# Verificar notas dos alunos já digitados

verif = 0
while verif != 999:
    alu = int(input("Informe a posição do aluno que você quer ver a anota (Digite 999 para) "))
    if alu == 999:
        break
    print(f"as notas do aluno(a) {geral[alu-1][0]} foram {geral[alu-1][1]} ")
    print("-=" * 30)
