# abstractmethod para qualquer método já decorado
# É possível criar @property @property.setter @classmethod
# @staticmethod e métodos normais como abstratos, para isso
# use @abstractmethod como decorator mais interno.
# Foo - Bar são palavras usadas como placeholder
# para palavras que podem mudar na programação.

from abc import ABC, abstractmethod

class AbstractFoo(ABC):
    def __init__(self, name):
        self.name = name

    @property
    def name(self): ...

    @name.setter
    def name(self, name): ...

class Foo(AbstractFoo):
    def __init__(self, name):
        super().__init__(name)
        print('Sou Inutil')

foo = Foo('Bar')
print(foo.name)