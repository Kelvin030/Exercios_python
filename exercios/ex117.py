# Exercicio: uma classe com base nos dados de uma Pessoa


class Pessoas:

    def __init__(self, nome, sexo, profissao):
        self.nome = nome
        self.sexo = sexo
        self.profissao = profissao
    
    def __str__(self):
        return f'Nome: {self.nome}\nSexo: {self.sexo}\nProfissão: {self.profissao}'

    def mostrar_trabalho(self):
        print(f'{self.nome} esta trabalhando como {self.profissao}')


if __name__ == '__main__':
    julia = Pessoas('Julia', 'Femenino', 'Medica')
    print(julia)
    julia.mostrar_trabalho()
    print('---------')
    jose = Pessoas('José', 'Masculino', 'Programador')
    print(jose)
    jose.mostrar_trabalho()