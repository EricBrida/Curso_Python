# Manipulando chaves e valores em dicionários

pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
    'idade': 18,
    'altura': 1.8,
    'endereços': [
        {'rua': 'tal tal', 'número': 123},
        {'rua': 'outra rua', 'número': 321},
    ]
}

del pessoa['endereços']
# print(pessoa['endereços']) -> KeyError, pois endereço foi deletado
print(pessoa.get('endereços', 'Não existe')) # Caso não exista printa não existe, caso contrario mostra os endereços
