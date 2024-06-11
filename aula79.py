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

pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
    'idade': 18,
    'altura': 1.8
}

print(len(pessoa))
print(list(pessoa.keys()))

# for chave in pessoa.keys():
#     print(chave)

print(list(pessoa.values()))

# for valor in pessoa.values():
#     print(valor)

print(list(pessoa.items()))

# for chave, valor in pessoa.items():
#     print(chave, ' -> ', valor)

pessoa.setdefault('olho', 'Azul')
print(pessoa['olho'])