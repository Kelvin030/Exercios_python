list = [[],[]]
for c in range(0, 7):
    x = int(input("Digite um valor: "))
    if x % 2 == 0:
        list[0].append(x)
    else:
        list[1].append(x)
print("-=" * 30)
print(f"Os valores PARES digitados foram: {sorted(list[0])} ")
print(f"E os valores IMPARES são: {sorted(list[1])}")
