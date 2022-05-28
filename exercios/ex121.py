import requests


#PokeApi
cont = 1
while True:
    url = requests.get(f'https://pokeapi.co/api/v2/pokemon/{cont}')
    pokemon = url.json()
    print(f'{cont} - {pokemon["name"]}')
    cont += 1
