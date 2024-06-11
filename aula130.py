# Mantendo estados dentro da classe

class Camera:
    def __init__(self, nome, filmando=False):
        self.nome = nome
        self.filmando = filmando

    def filmar(self):

        if self.filmando:
            print('Ja está filmando')
            return

        print(f'{self.nome} está filmando')
        self.filmando = True

    def parar_filmar(self):

        if not self.filmando:
            print('Ja não está filmando...')
            return

        print(f'{self.nome} parou de filmar')
        self.filmando = False

    def fotografar(self):
        if self.filmando:
            print('Não é possivel tirar foto enquanto filma...')
            return
        
        print('Foto tirada com sucesso...')
        

c1 = Camera('Logitech')
c2 = Camera('Sony')

c1.filmar()
c1.parar_filmar()
c1.parar_filmar()
# c1.filmar()

c1.fotografar()

print(c1.filmando)
# print(c2.filmando)