def notas(*n, sit=False):
    """
    --> Função para analizar nota e situação de um aluno(a)
    :param n: Uma ou mais notas do aluno(a)
    :param sit: Valor opcional indicando a situação do aluno(a)
    :return: Dicionario com varias informaçoes do aluno(a)
    """
    situação = dict()

    situação['total'] = len(n)
    situação['maior'] = max(n)
    situação['menor'] = min(n)
    situação['media'] = (sum(n)) / len(n)
    if sit:
        if situação['media'] <= 5:
            situação['situação'] = 'RUIM'
        elif situação['media'] < 7:
            situação['situação'] = 'RAZOÁVEL'
        elif situação['media'] >= 8:
            situação['situação'] = 'BOM'
    return situação


# Programa Principal
notas(5, 7, 3, sit=True)
