list = []
while True:
    list.append(int(input("digite um valor: ")))
    continue_ = str(input('Deseja continuar? [S/N]')).upper()
    if continue_ == "N":
        break
print("=-" * 40)
print(f"Foram digitados {len(list)} valores")
print(f"os valores digitados em forma decresente são {sorted(list,reverse=True)}")
if 5 in list:
    print(f"o numero 5 foi digitado ")
else:
    print("o numero 5 NÃO foi digitado")
