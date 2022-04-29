num = []
for c,n in enumerate(range(0, 5)):
    num.append((int(input(f'Digite um valor, na {c}° posição: '))))
print("=-" * 50)
print(f'O maior valor digitado foi {max(num)}, na posição {num.index(max(num))}')
print(f'O menor valor digitado foi {min(num)}, na posição {num.index(min(num))}')
num.sort()
print(f"Os valores diditados em ordem é {num}")

