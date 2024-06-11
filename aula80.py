# Métodos úteis para dicionários em Python
# len -> quantas chaves
# keys -> iteravel com as chaves
# values -> iteravel com os valores
# items -> iteravel com as chaves e valores
# setdefault -> adiciona valor se a chave não existe
# copy -> retorna uma copia rasa (shallow copy)
# get -> obtem uma chave
# pop -> apaga um item com a chave especificada (del)
# popitem -> apaga o ultimo item adicionado
# update -> atualiza um dicionario com outro

import copy

d1 = {

    'c1': 1,
    'c2': 2,
    'l1': [0, 1, 3]

}

d2 = d1.copy() # Copia Rasa, altera valores mutaveis, como no caso da list
d3 = copy.deepcopy(d1) # Copia Profunda, não altera nenhum valor mutavel

d2['c1'] = 1000
d3['c1'] = 1000
d2['l1'][1] = 2 # Altera o valor de todos os que estiverem relacionados, Copia Rasa
d3['l1'][1] = 9999 # Altera o valor de d3 apenas, Copia profunda

print('2 -> ', d2)
print('3 -> ', d3)
print('1 -> ', d1)

