# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela

class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None

    def inserir_motor_e_fabricante(self, motor, fabricante):
        self._motor = motor
        self._fabricante = fabricante

    def listar_carro(self):
        print(f'Carro -> {self.nome} | Motor -> {self._motor.nome} | Fabricante -> {self._fabricante.nome}', end='\n\n')

class Motor:
    def __init__(self, nome):
        self.nome = nome

class Fabricante:
    def __init__(self, nome):
        self.nome = nome

c1 = Carro('Camaro')
m1 = Motor('V8')
f1 = Fabricante('Chevrolet')

c2 = Carro('Mustang')
f2 = Fabricante('Ford')

c1.inserir_motor_e_fabricante(m1, f1)
c1.listar_carro()

c2.inserir_motor_e_fabricante(m1, f2)
c2.listar_carro()