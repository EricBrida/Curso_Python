# Atributos de Classe

# ANO_ATUAL = 2024

class Pessoa:
    ano_atual = 2024

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nasc(self):
        return self.ano_atual - self.idade
    
p1 = Pessoa('João', 35)

p1.__dict__['outra'] = 'coisa'
p1.__dict__['nome'] = 'Teste'

print(p1.__dict__)
print(vars(p1))