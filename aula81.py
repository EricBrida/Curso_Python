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

p1 = {
    'nome': 'Eric',
    'sobrenome': 'Brida',
}

# nome = p1.pop('nome')
# print(nome)
# print(p1)

# nome = p1.popitem()
# print(nome)
# print(p1)

lista = [['nome', 'João'], ['idade', 30]]
p1.update(lista)
print(p1)
