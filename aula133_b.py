import json

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

with open('aula133.json', 'r', encoding='utf-8') as arquivo:
    dados = json.load(arquivo)

p1 = Pessoa(**dados)

print(vars(p1))
print(p1.nome)
print(p1.idade)