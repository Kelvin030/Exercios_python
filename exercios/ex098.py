def contador(start, stop, step):
    from time import sleep
    if step < 0:
        step = step * -1
    if start > stop:
        step = step * -1
    if stop > 0:
        stop += 1
    print(f"Contador de {start} ate {stop} de {step} em {step}")
    print('=' * 60)
    cont = 0
    for c in range(start, stop, step):
        print(c, end=' ')
        cont += 1
        if cont > 20:
            print()
            cont = 0
        sleep(0.3)
    print("<<<FIM>>>")
    print('=' * 60)


# Principal
contador(0, -10, 1)
contador(10, 0, 2)
print("Agora é sua vez!!!")
incio = int(input("Inicio: "))
fim = int(input("Fim: "))
passo = int(input("Passo: "))
contador(incio, fim, passo)
