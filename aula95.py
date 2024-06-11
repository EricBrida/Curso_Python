# dir, hasattr e getattr em Python

string = 'Luiz'
metodo = 'upper'

if hasattr(string, metodo):
    print('Existe Upper')
    print(getattr(string, metodo)())
else:
    print('Não existe o método', metodo)