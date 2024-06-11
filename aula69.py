"""
Valores padrão para parâmetros
Ao definir uma função, os parâmetros podem
ter valores padrão. Caso o valor não seja
enviado para o parâmetro, o valor padrão será
usado.
Refatorar -> Editar o seu código.
"""

def soma(x, y, z=None):
    if z is None:
        print(f'{x=} {y=} |', x + y)
    else:
        print(f'{x=} {y=} {z=} |', x + y + z)

soma(10, 2, 0)
soma(5, 6, 8)
soma(60, 80)
soma(z=7, x=3, y=2)
soma(1, 1)