from requests import get
try:
    resposta = get('http://pudim.com.br/')
except:
    print('O site pudim NÃO esta acessivel no momento')
else:
    print('Consegui acessar o site Pudim com sucesso!!!')
