# Problema dos parâmetros mutáveis em funções Python

def adiciona_clientes(nome, lista=None):

    if lista is None:
        lista = []

    lista.append(nome)
    return lista


cliente1 = adiciona_clientes('Eric')
adiciona_clientes('Joana', cliente1)

cliente2 = adiciona_clientes('Julio')
adiciona_clientes('Elena', cliente2)


print(cliente1)
print(cliente2)