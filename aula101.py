# raise -> lançando exceções (erros)
# # https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions

def nao_aceito_zero(d):
        
    if d == 0:
        raise ZeroDivisionError('Não divida por Zero')
    return True

def verifica_int_float(num):

    tipo_num = type(num)

    if not isinstance(num, (float, int)):
        raise TypeError(f'{num} deve ser int ou float \n {tipo_num} enviado')
    
    return True

def divide(n, d):

    verifica_int_float(n)
    verifica_int_float(d)

    nao_aceito_zero(d)
    
    return n / d
    
print(divide(8, 0))