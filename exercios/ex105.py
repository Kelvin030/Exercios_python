def notas(*n, sit=False):
    situação = dict()

    situação['total'] = len(n)
    situação['maior'] = max(n)
    situação['menor'] = min(n)
    situação['media'] = (sum(n)) / len(n)
    if sit == True:
        if situação['media'] <= 5:
            situação['situação'] = 'RUIM'
        elif situação['media'] < 7:
            situação['situação'] = 'RAZOÁVEL'
        elif situação['media'] >= 8:
            situação['situação'] = 'BOM'
    print(situação)


# Programa Principal
notas(5, 7, 3, sit=True)
