# Métodos da classe + factories
# São métodos onde "self" será "cls", ou seja,
# ao invés de receber a instância no primeiro
# parâmetro, receberemos a própria classe.

class Pessoa:
    ano = 2024 # Atributo de classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def metodo_de_classe(cls):
        print('Hey')

    @classmethod
    def criar_com_50_anos(cls, nome):
        return cls(nome, 50)
    
    @classmethod
    def criar_sem_nome(cls, idade):
        return cls('Anônima', idade)

print(Pessoa.ano)

p1 = Pessoa('Eric', 19)
p2 = Pessoa.criar_com_50_anos('Carlos')
p3 = Pessoa.criar_sem_nome(22)

print(p1.nome, p1.idade)
print(p2.nome, p2.idade)
print(p3.nome, p3.idade)

# Pessoa.metodo_de_classe()
