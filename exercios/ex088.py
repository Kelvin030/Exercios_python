from random import choice
from time import sleep
list = []
x = []

print("-" * 40)
print("Gerador de palpites".center(40))
print("-" * 40)
quant = int(input("Digite a quantidade de palpites: "))

# Geração de numeros aleatorios 

for q in range(0, quant):
    for c in range(0, 6):
        x.append(choice(range(1, 60)))
    list.append(x.copy())
    x.clear()


# retorno das informações para o usuario

print(f" SORTEANDO {quant} JOGOS ".center(40,"="))
sorted(list)
for i, l in enumerate(list):
    print(f"Jogo {i+1}: {l}")
# O objetivo do "sleep" é para o usuario ter uma sensação de que os numeros estão sendo gerados
    sleep(0.5)
