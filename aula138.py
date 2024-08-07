# @property e @setter -> getter e setter no modo Python
# -> como getter
# -> p/ evitar quebrar código do cliente
# -> p/ habilitar setter
# -> p/ executar ações ao obter um atributo
# Atributos que começam com _ ou __, não devem ser usados
# fora da classe.

class Caneta():
    def __init__(self, cor):
        self._cor = cor
        self._cor_tampa = None

    @property
    def cor(self):
        print('Property')
        return self._cor
    
    @cor.setter
    def cor(self, valor):
        print('Setter')
        self._cor = valor

    @property
    def cor_tampa(self):
        return self._cor_tampa
    
    @cor_tampa.setter
    def cor_tampa(self, valor):
        self._cor_tampa = valor

    
def mostrar_caneta(caneta):
    return [caneta.cor, caneta.cor_tampa]

caneta = Caneta('Azul')
caneta.cor = 'Azul'
caneta.cor_tampa = 'Azul'
print(mostrar_caneta(caneta))