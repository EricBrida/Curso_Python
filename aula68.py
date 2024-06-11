"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""

# Definição
def soma(x, y):
    print(f'{x=} + {y=} | ', x + y)

soma(y=1, x=2)
soma(8, 9)
