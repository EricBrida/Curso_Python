"""
Iterável -> str, range, etc (__iter__)
Iterador -> Quem sabe entregar um valor por vez
next -> Me entregue o próximo valor
iter -> Me entregue seu iterador
"""

# texto = iter('Eric') # __iter__()
# print(texto)

# print(next(texto)) # __next__()
# print(next(texto))
# print(next(texto))
# print(next(texto))
# print(next(texto)) # StopIteration

texto = 'Eric' # Iterável
iterador = iter(texto) # Iterador

while True:
    try:
        print(next(iterador))
    except StopIteration:
        print('Acabou')
        break
