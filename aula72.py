"""
args -> Argumentos não nomeados
* - *args (empacotamento e desempacotamento)
"""

# Lembrete de desempacotamento
x, y, *resto = 1, 2, 3, 4
print(x, y, resto)

def soma(*args):
    # args = list(args)
    total = 0

    for num in args:
        total += num

    return total

soma1 = soma(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(soma1)

numeros = 50, 77, 23, 41, 91, 85
soma2 = soma(*numeros)
print(soma2)

print(sum((50, 77, 23, 41, 91, 85))) # Função de soma do Python
print(sum(numeros))