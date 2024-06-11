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
p2 = Pessoa('Helena', 12)

print(p1.get_ano_nasc())
print(p2.get_ano_nasc())