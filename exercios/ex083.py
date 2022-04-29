aberto = 0
fechado = 0
expre = input("Digite a expressão: ")
for i in expre:
    if i == "(":
        aberto += 1
    elif i == ")":
        fechado += 1
r = aberto + fechado
if r % 2 == 0:
    print("essa expressão esta valida!!")
else:
    print("expressão invalida")
