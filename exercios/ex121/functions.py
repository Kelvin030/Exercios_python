import requests


class SearchPokemon:
    def __init__(self,indice):
        try:
            self.url = requests.get(f'https://pokeapi.co/api/v2/pokemon/{indice}')
            self.response = self.url.json()
        except requests.exceptions.JSONDecodeError:
            print('Pokemon não encontrado...')
            quit()
        except Exception as erro:
            print(f'Ocorreu um problema: {erro}')
            quit()

    def pokemon(self):

        self.name = self.response['name']
        self.base_stats = {"HP": self.response['stats'][0]['base_stat'],
                          'Attack': self.response['stats'][1]['base_stat'],
                          'defense': self.response['stats'][2]['base_stat'],
                          'special-attack': self.response['stats'][3]['base_stat'],
                          'special-defense': self.response['stats'][4]['base_stat'],
                          'speed': self.response['stats'][5]['base_stat']}

        # Tipo do pokemon
        self.types = []
        for type in self.response['types']:
             self.types.append(type['type']['name'])

        # Imagem do pokemon
        self.sprite = self.response['sprites']['front_default']

        # Movimentos do pokemon
        self.moves = []
        for move in self.response['moves']:
            self.moves.append(move['move']['name'])

        # Abilidades
        self.abilities = []
        for abilitie in self.response['abilities']:
            self.abilities.append(abilitie['ability']['name'])

        # Jogos em que o pokemon aparece
        self.game_indices = []
        for game in self.response['game_indices']:
            self.game_indices.append(game['version']['name'])

        # Taxa de captura
        species = requests.get(self.response['species']['url'])
        self.capture_rate = species.json()['capture_rate']


    def show_search(self):
        print(f'Nome: {self.name}')
        print('Tipos:', end=' ')
        for Type in self.types:
            print(Type,end=' ')
        print()
        print(f'Status Basicos:')
        print(self.base_stats)



def list_pokemoms_id():
    with open('pokemons.txt', 'r') as file:
        print(file.read())


if __name__ == '__main__':
    teste = SearchPokemon(1)
    teste.pokemon()
    teste.show_search()