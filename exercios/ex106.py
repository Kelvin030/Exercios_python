while True:
    comand = str(input("Função ou biblioteca: "))
    if comand == 'fim':
        break
    help(comand)

"""Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help do Python.
 O usuário vai digitar o comando e o manual vai aparecer.
 Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará.
"""