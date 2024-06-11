# Closure e Funções que retornam outras funções

def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar

s1 = criar_saudacao('OIoioi')
s2 = criar_saudacao('Tchauthcau')

for nome in ['Maria', 'Jose', 'Carlos', 'Rodolfo']:
    print(s1(nome))