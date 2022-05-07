def maior(*num):
    maior_num = 0
    if len(num) == 0:
        maior_num = 'NÃO EXISTE'
    else:
        maior_num = max(num)
    print("Analizando valores passados...")
    for n in num:
        print(n, end=' ')
    print(f'Foram informados {len(num)} valores ao todo.')
    print(f"O maior valor informado foi {maior_num}")
    print('-=' * 30)


# Principal
maior(1, 4, 99, 12)
