# class -> Classes são moldes para criar novos objetos
# As classes geram novos objetos (instâncias) que 
# podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de 
# classes.

# string = 'Eric' # str
# print(string.upper())
# print(isinstance(string, str))

class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

p1 = Pessoa('Eric', 'Brida')
# p1.nome = 'Eric'
# p1.sobrenome = 'Brida'

p2 = Pessoa('Carlos', 'Gonçalves')
# p2.nome = 'Carlos'
# p2.sobrenome = 'Gonçalves'

print(p1.nome)
print(p1.sobrenome)
print(p2.nome)
print(p2.sobrenome)