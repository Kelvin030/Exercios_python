def LeiaDinheiro(msg):
    validação = False
    while not validação:
        valor = input(msg).replace(',', '.').strip()
        if valor.isalpha():
            print(f'ERRO!!! \033[91m"{valor}"\033[m é um preço invalido')
        else:
            validação = True
    return float(valor)
