# Retorno de valores das Funções (return)

def soma(x, y):

    if x > 10:
        return 'Abacate'
    return x + y # Faz a função retorna 'x + y' ao invez de None

variavel = soma(1, 3) # Recebe o 'return x + y'
variavel_2 = soma(11, 3)
print(variavel)
print(variavel_2)