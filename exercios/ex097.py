def escreva(msg, caractere):

    print(caractere * (len(msg) + 4))
    print(f"{msg}".center(len(msg) + 4))
    print(caractere * (len(msg) + 4))


# Programa Principal
escreva('Teste', '=')
