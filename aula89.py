# Empacotamento e Desempacotamento de dicionários

a, b = 1, 2
a, b = b, a
print(a, b)

pessoa = {

    'nome': 'Aline',
    'sobrenome': 'Souza',

}

dado_completo = {

    'idade': 16,
    'altura': 1.6

}

pessoa_completa = {**pessoa, **dado_completo}

# print(pessoa_completa)

# a, b = pessoa.values()
# print(a, b) # Aline Souza

# args e kwargs
# args
# kwargs -> keyword arguments (argumentos nomeados)

def mostro_argumentos_nomeados(*args, **kwargs):
    print('Não Nomeados -> ', args)

    for chave, valor in kwargs.items():
        print(chave, valor) 

# mostro_argumentos_nomeados('teste', 123, 'Oi', nome='Joana', qlqr = 123)
# mostro_argumentos_nomeados(**pessoa_completa)

configuracoes = {

    'arg1': 1,
    'arg2': 2,
    'arg3': 3,
    'arg4': 4,

}

mostro_argumentos_nomeados('oi', 'teste', 123, **configuracoes)
