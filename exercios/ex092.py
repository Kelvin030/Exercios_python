from datetime import date
dados = dict()

dados['nome'] = input('NOME: ').strip().capitalize()
dados['idade'] = date.today().year - int(input('DATA NASCIMENTO: '))
dados['ctps'] = int(input('Nº CARTEIRA DE TRABALHO (0 se não tem): '))

if dados['ctps'] > 0:
    dados['contratação'] = int(input('ANO DE CONTRATAÇÃO: '))
    dados['salário'] = float(input('SALÁRIO: R$'))
    dados['aposentadoria'] = dados['contratação'] - (date.today().year - dados['idade']) + 35

print()
print("Informações".center(50, '='))
for chave, valor in dados.items():
    print(f'{chave}: {valor}')
