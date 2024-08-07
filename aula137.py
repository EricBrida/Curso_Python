# @property - um getter no modo Pythonico
# getter - um método para obter um atributo
# modo pythônico - modo do Python de fazer coisas
# @property é uma propriedade do objeto, ela
# é um método que se comporta como um
# atributo
# Geralmente é usada nas seguintes situações:
# -> como getter
# -> p/ evitar quebrar código do cliente
# -> p/ habilitar setter
# -> p/ executar ações ao obter um atributo

class Caneta:
    def __init__(self, cor):
        self.cor_tinta = cor 

    @property
    def cor(self):
        print('Property')
        return self.cor_tinta
    
    @property
    def cor_tampa(self):
        return 123456

    # def get_cor(self):
    #     return self.cor

caneta = Caneta('Azul')
print(caneta.cor)
print(caneta.cor_tampa)