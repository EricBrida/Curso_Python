"""
split e join com list e str
split -> divide uma string
join -> une uma string
"""

frase = 'Olha só que, coisa interessante'
lista_palavras_cruas = frase.split(',')

lista_frase = []

for i, frases in enumerate(lista_palavras_cruas):
    lista_frase.append(lista_palavras_cruas[i].strip())

# print(lista_frase)

frases_unidas = ', '.join(lista_frase)
print(frases_unidas)
