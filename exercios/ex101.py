def voto(ano):
    from datetime import date
    hoje = date.today().year
    idade = hoje - ano
    if idade >= 18 and idade <= 64:
        return 'VOTO OBRIGATORIO!!!'
    elif idade < 18:
        return 'VOTO OPCIONAL'
    elif idade > 64:
        return 'VOTO OPCIONAL'


# Programa Principal
ano = int(input("Digite seu ano de nacimento: "))
print(voto(ano))
