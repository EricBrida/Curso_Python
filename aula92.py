# Dictionary Comprehension e Set Comprehension

produto = {

    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritório',

}

# for chave, valor in produto.items():
#     print(chave, ' -> ', valor)

dc = {
    chave: valor.upper()
    if isinstance(valor, str) else valor
    for chave, valor
    in produto.items()
    if chave != 'categoria' # Não Mostra 'categoria'
}

print(dc)

lista = [

    ('a', 'valor a'),
    ('b', 'valor b'),
    ('b', 'valor b'),

]

# dc = {
#     chave: valor 
#     for chave, valor in lista
# }

# print(dc)
print(dict(lista), end='\n\n\n')

s1 = {2 ** i for i in range(10)}

print(s1)