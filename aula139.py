# Encapsulamento (Modificadores de acesso, public, private e protected)
# Python NÂO TEM modificadores de acesso
# Mas podemos seguir as seguintes convenções 
#   (Sem Underline) = public
#       Pode ser usado em qualquer lugar
#  _(Um Underline) = protected
#       não DEVE ser usado fora da classe
#       ou suas subclasses.
# __(Dois Underlines) = private
#       "name mangling" (desconfiguração de nomes) em Python
#       só DEVE ser usado na classe em que foi
#       declarado.

class Foo:
    def __init__(self):
        self.public = 'Isso é publico'
        self._protected = 'Isso é protegido'
        self.__private = 'Isso é privado'

    def metodo_publico(self):
        return 'metodo publico'
    
    def _metodo_protected(self):
        return 'metodo protegido'
    
    def __metodo_private(self):
        return 'metodo private'

f = Foo()
print(f.public)
print(f.metodo_publico())
print(end='\n\n')
print(f._protected)
print(f._metodo_protected())
print(end='\n\n')
# print(f.__private)
print(f._Foo__metodo_private())