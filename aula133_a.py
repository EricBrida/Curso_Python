# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.

import json

class Pessoa:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        

p1 = Pessoa('Eric', 19)
dados = vars(p1)

with open('aula133.json', 'w', encoding='utf-8') as arquivo:
    json.dump(dados, arquivo, indent=2)