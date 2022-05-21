#Primeiro programa com API
import requests
from json import loads

def requisição_cep(cep):
    url = requests.get(f'https://cep.awesomeapi.com.br/JSON/{cep}')
    requisição = loads(url.text)
    try:
        print(f'\nEndereço: {requisição["address"]}')
    except:
        print(f'Erro: {requisição["status"]}, {requisição["message"]}')
    else:
        print(f'Cidade: {requisição["city"]}')
        print(f'Distrito: {requisição["district"]}')
        print(f'Estado: {requisição["state"]}')
        print(f'DDD: {requisição["ddd"]}')


print('=' * 40)
print('Verificador de CEP'.center(40))
print('=' * 40)
while True:
    try:
        cep = int(input("Digite um cep (Somente numeros): "))
    except:
        print('Erro! tente novamente...')
    else:
        break

requisição_cep(cep)
