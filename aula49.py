"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append, insert, pop, del, clear, extend, +
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""

#        0   1   2   3   4   5   6
lista = [10, 20, 30, 40, 50, 60, 70]

# lista[2] = 300
# del lista[2]
# print(lista)
# print(lista[2]) # Printa 40

lista.append(80) # Adiciona 80 ao final da lista
ultimo = lista.pop(2) # Remove o último valor da lista caso não especificado
print(lista, ' Removido ', ultimo)

