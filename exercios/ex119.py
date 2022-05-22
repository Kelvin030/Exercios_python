def requisição(moeda1='USD'):
    from requests import get
    from json import loads
    try:
        url = get(f'https://economia.awesomeapi.com.br/json/last/{moeda1}-BRL')
    except Exception as erro:
        print(f'Ocorreu o erro: {erro}')
    else:
        return loads(url.text)


def BTCBRL(dic):
    print('COTAÇÃO: R${}'.format(dic["BTCBRL"]["low"]))
    print('DATA: {}'.format(dic["BTCBRL"]["create_date"]))


def USDBRL(dic):
    print('COTAÇÃO: R${}'.format(dic["USDBRL"]["low"]))
    print('DATA: {}'.format(dic["USDBRL"]["create_date"]))


def EURBRL(dic):
    print('COTAÇÃO: R${}'.format(dic["EURBRL"]["low"]))
    print('DATA: {}'.format(dic["EURBRL"]["create_date"]))


print('=' * 40)
print('Cotação Moedas'.center(40))
print('=' * 40)
print('Deseja ver a cotação de qual moeda:')
print('1 - BTC')
print('2 - USD')
print('3 - EUR')
print('4 - sair')
print('=' * 40)
while True:
    while True:
        try:
            escolha = int(input('Sua opção: '))
        except:
            print("erro tente novamente...")
        else:
            break
    if escolha == 1:
        BTCBRL(requisição('BTC'))
        break
    elif escolha == 2:
        USDBRL(requisição('USD'))
        break
    elif escolha == 3:
        EURBRL(requisição('EUR'))
        break
    elif escolha == 4:
        print('Volte sempre!!!')
        break
    else:
        print('opção invalida...')
