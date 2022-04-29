dados = []
pass_ = []
cont = 0
while True:
    pass_.append(str(input("Digite seu nome: ")))
    pass_.append(float(input("Digite seu peso (Kg): ")))
    dados.append(pass_.copy())
    pass_.clear()
    cont += 1
    resp = str(input("Deseja continuar[S/N]:")).upper()
    if resp == "N":
        break

print("=-" * 40)
print(f"Foram cadastrados {cont} pessoas")
