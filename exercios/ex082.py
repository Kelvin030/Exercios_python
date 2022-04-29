list = []
pares = []
impar = []
while True:
    x = (int(input("digite um valor: ")))
    continue_ = str(input("deseja continuar? [S/N]")).upper()
    if x % 2 == 0:
        pares.append(x)
    elif x % 2 == 1:
        impar.append(x)
    if continue_ == "N":
        break
list += pares + impar
print(f"pares: {pares}")
print(f"impar: {impar}")
print(f"A lista completa é: {sorted(list)}")
