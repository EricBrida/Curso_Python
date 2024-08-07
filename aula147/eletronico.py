from log import LogPrintMixin

class Eletronico(LogPrintMixin):
    def __init__(self, nome):
        self._nome = nome
        self._ligado = False

    def ligar(self):
        if not self._ligado:
            print(f'Ligando o {self.__class__.__name__} {self._nome}')
            self._ligado = True
            msg = f'{self.__class__.__name__} ligado com exito'
            self.log_sucess(msg)
            return
        
        print(f'O {self.__class__.__name__} {self._nome} já está ligado')

    def desligar(self):
        if self._ligado:
            print(f'Desligando o {self.__class__.__name__} {self._nome}')
            self._ligado = False
            msg = f'{self.__class__.__name__} desligado com exito'
            self.log_sucess(msg)
            return
        
        print(f'O {self.__class__.__name__} {self._nome} já está desligado')

class Smartphone(Eletronico):
    ...

        
