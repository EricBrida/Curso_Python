# Relações entre classes: Associação, agregação e composição
# Composição é uma especialização da agregação
# Mas nela, quando o objeto "pai" for apagado, todas
# as referências dos objetos filhos tambem são
# apagadas.

class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self._enderecos = []

    def inserir_endereco(self, rua, numero):
        self._enderecos.append(Endereco(rua, numero))

    def inserir_endereco_externo(self, endereco):
        self._enderecos.append(endereco)

    def listar_endereco(self):
        for i, endereco in enumerate(self._enderecos):
            print(f'Endereço {i + 1} | Rua - {endereco.rua}, Numero - {endereco.numero}')

    def __del__(self):
        print(f'Apagando {self.nome}')

class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero

    def __del__(self):
        print(f'Apagando {self.rua}, {self.numero}')

c1 = Cliente('Maria')
c1.inserir_endereco('Av Brasil', 54)
c1.inserir_endereco('Rua 78', 76)
end_ext = Endereco('Carlim 23', 78)
c1.inserir_endereco_externo(end_ext)
c1.listar_endereco()

del c1

print(end='\n\n')
print('####################### FIM #######################', end='\n\n')