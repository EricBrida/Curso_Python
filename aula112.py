# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

# def criar_funcao(func):
#     def junta_lista(a, b):
#         res = func(a, b)
#         mostra = f'{res}. Foi a lista gerada'

#         return mostra
#     return junta_lista

# @criar_funcao
# def zipper(a, b):
#     size = (min(len(a), len(b)))

#     return [

#         (a[i], b[i]) for i in range(size)

#     ]
        

    

# lista1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
# lista2 = ['BA', 'SP', 'MG', 'RJ']

# lista_modificada = zipper(lista1, lista2)

# print(lista_modificada)

from itertools import zip_longest

lista1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
lista2 = ['BA', 'SP', 'MG', 'RJ']

print(list(zip(lista1, lista2)))
print(list(zip_longest(lista1, lista2, fillvalue='Sem Cidade')))
