def escreva(msg, caractere):
    print(caractere * (len(msg) + 6))
    print(f"{msg}".center(len(msg) + 6))
    print(caractere * (len(msg) + 6))


# Programa Principal
escreva('Teste', '=')
