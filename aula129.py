# Escopo da classe e de métodos da classe

class Animal:
    # nome = 'Leão'

    def __init__(self, nome):
        self.nome = nome

    # variavel = 'valor'
    # print(variavel)

    def comendo(self, alimento='nada'):
        print(f'{self.nome} está comendo {alimento}')

leao = Animal('Leão')
print(leao.nome)
leao.comendo('coco')
