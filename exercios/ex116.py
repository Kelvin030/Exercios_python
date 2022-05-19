"""EXERCICIO: Crie um software de gerenciamento bancario
Esse software pode ser capaz de criar um cliente e conta
Cada cliente possui Nome, Idade, e CPF
Cada conta possui um cliente, saldo, limite, sacar, depositar e consultar saldo"""


class Cliente:
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf


class Conta:
    def __init__(self, cliente, saldo, limite):
        self.cliente = cliente
        self.saldo = saldo
        self.limite = limite * -1

    def sacar(self, valor):
        if self.saldo - valor < self.limite:
            return 'Saldo insuficiente'
        else:
            self.saldo = self.saldo - valor
            return 'Saque feito com suscesso!'

    def depositar(self, valor):
        if valor < 1:
            return 'Valor digitado invalido'
        else:
            self.saldo = valor + self.saldo
            return 'Deposito feito com suscesso!'

    def consultar_saldo(self):
        return f'O saldo em conta é R${self.saldo:.2f}'.replace('.', ',')


if __name__ == '__main__':
    cliente1 = Cliente('Julio', 27, '568.487.355-97')
    conta1 = Conta(cliente1, 78, 1000)
    print(conta1.consultar_saldo())
    print(conta1.depositar(95))
    print(conta1.consultar_saldo())
    print(conta1.sacar(1000))
    print(conta1.consultar_saldo())
