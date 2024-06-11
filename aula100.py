# Try, except, else e finally

try:
    print('Abriu')
    8/0
except ZeroDivisionError:
    print('Dividiu por Zero')
else:
    print('Não deu Erro')
finally:
    print('Fechou')