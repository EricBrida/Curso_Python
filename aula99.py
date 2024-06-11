# Try, except, else e finally

try:
    a = 18
    b = 0
    print(b[0])
    c = a / b # Divisão por Zero -> ZeroDivisionError
except ZeroDivisionError:
    print('Não divida por Zero')
except NameError:
    print('Variavel não definida')
except (TypeError, IndexError) as error:
    print('TypeError | IndexError')
    print('MSG: ', error)
    print('Nome: ', error.__class__.__name__)
except Exception:
    print('Erro Desconhecido...')