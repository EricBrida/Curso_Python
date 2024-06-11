import json

# pessoa = {

#     'nome': 'Eric',
#     'sobrenome': 'Brida',
#     'enderecos': [

#         {'rua': 'R1', 'numero': 123},
#         {'rua': 'R2', 'numero': 456},

#     ],

#     'altura': 1.65,
#     'numeros_preferidos': (2, 4, 6, 8, 10),
#     'dev': True,
#     'nada': None,

# }

# with open('aula123.json', 'w', encoding='utf-8') as arquivo:
#     json.dump(pessoa, arquivo, indent=2)

with open('aula123.json', 'r', encoding='utf-8') as arquivo:
    pessoa = json.load(arquivo)

print(pessoa)
print(type(pessoa))