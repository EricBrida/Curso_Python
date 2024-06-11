# reduce -> faz a redução de um iterável em um valor

from functools import reduce

produtos = [  

    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 20.00},
    {'nome': 'Produto 3', 'preco': 30.00},
    {'nome': 'Produto 2', 'preco': 20.00},
    {'nome': 'Produto 4', 'preco': 10.00},

]

# total = 0
# for p in produtos:
#     total += p['preco']

# print(round(total, 2))

# print(sum([p['preco'] for p in produtos]))

def funcao_do_reduce(total, produto):
    print(total)
    print(produto)
    return total + produto['preco']

total = reduce(

    # lambda tt, p: tt + p['preco'],
    funcao_do_reduce,
    produtos,
    0

)

print(f'Preço Total -> {round(total, 2)}')