# super() é a super classe na sub classe
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class

# class MinhaString(str):
#     def upper(self):
#         print('Chamou UPPER')
#         retorno = super().upper()
#         print('Depois do UPPER')
#         return retorno
    
# string = MinhaString('Trivago')
# print(string.upper())

class A:
    atributo_a = 'valor'

    def __init__(self, atributo):
        self.atributo = atributo

    def metodo(self):
        print('A')

class B(A):
    atributo_b = 'valor'

    def __init__(self, atributo, outra_coisa):
        super().__init__(atributo)
        self.outra_coisa = outra_coisa

    def metodo(self):
        # super().metodo()
        print('B')
 
class C(B):
    atributo_c = 'valor'

    def metodo(self):
        # super().metodo()
        A.metodo(self)
        B.metodo(self)
        print('C')

# print(C.mro())

c = C('Atributo', 'Qualquer')

print(c.atributo)
print(c.outra_coisa)
c.metodo()

# print(c.atributo_a)
# print(c.atributo_b)
# print(c.atributo_c)
# c.metodo()

