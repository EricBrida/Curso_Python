# Valores Truthy e Falsy, Tipos Mutáveis e Imutáveis
# Mutáveis -> [] {} set()
# Imutáveis -> () "" 0 0.0 None False range(0,10)

lista = []
dic = {}
conjunto = set()
tupla = ()
string = ''
innt = 0
flooat = 0.0
nada = None
falso = False
intervalo = range(0)

def falsy(valor):
    return 'falsy' if not valor else 'truthy'

print('TESTE')
print(f'{lista=}', falsy(lista))
print(f'{dic=}', falsy(dic))
print(f'{conjunto=}', falsy(conjunto))
print(f'{tupla=}', falsy(tupla))
print(f'{string=}', falsy(string))
print(f'{innt=}', falsy(innt))
print(f'{flooat=}', falsy(flooat))
print(f'{nada=}', falsy(nada))
print(f'{falso=}', falsy(falso))
print(f'{intervalo=}', falsy(intervalo))