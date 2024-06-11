"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""

#        0   1   2   3
lista = [10, 20 ,30 ,40]
lista.append('Luiz')
nome = lista.pop()
lista.append(1233)
del lista[-1] # -1 Sempre vai ser o último item da lista
# lista.clear() # Limpa a lista
lista.insert(200, 5)
print(lista, nome)