# Exercício -> Exiba os indices da lista

lista = ['Maria', 'Helena', 'Luiz']
# i = 0

# for nome in lista:

#     print(i, ' - ', nome)
#     i += 1

lista.append('João')
indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice], type(lista[indice]))