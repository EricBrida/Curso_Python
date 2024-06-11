# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

import random

def multiplicador(multiplicador):
    def multiplicar(num):
        return f'{num} * {multiplicador} = {num * multiplicador}'
    return multiplicar

numero_multiplicador = multiplicador(random.randint(2, 4))
print(numero_multiplicador(random.randint(1, 10)))
