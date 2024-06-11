# Combinations, Permutations e Product - Itertools
# Combinação -> Ordem não importa - iterável + tamanho do grupo
# Permutação -> Ordem importa
# Produto -> Ordem importa e repete valores únicos

def sep(iterator):
    print(*list(iterator), sep='\n')
    print()

from itertools import combinations, permutations, product

pessoas = [
    'João', 'Joana', 'Luiz', 'Letícia'
]

camisetas = [
    ['preta', 'branca'],
    ['p', 'm', 'g'],
    ['masculino', 'feminino', 'unisex'],
    ['algodão', 'poliéster'],
]

sep(combinations(pessoas, 2))
sep(permutations(pessoas, 2))
sep(product(*camisetas))