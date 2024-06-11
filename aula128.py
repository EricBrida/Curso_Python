# Métodos em instâncias de classes Python
# Hard Coded -> Algo que foi escrito diretamente no código

class Carro:
    def __init__(self, nome):
        self.nome = nome

    def acelerar(self):
        print(f'O {self.nome} está acelerando')

fusca = Carro('Fusca')
celta = Carro('Celta')

print(fusca.nome)
print(celta.nome)

fusca.acelerar()