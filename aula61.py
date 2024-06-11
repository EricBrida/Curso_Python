# Listas de listas e seus índices

salas = [
    #   0        1
    ['Maria', 'Helena', ], # 0
    #   0   
    ['Elaine', ], # 1
    #   0       1        2               3
    ['Luiz', 'João', 'Eduarda', (0, 10, 20, 30, 40) ], # 2
    #                            0   1   2   3   4
]

print(salas[2][1]) # João -> Primeiro o índice da lista, depois o índice do valor desejado 
print(salas[2][2]) # Eduarda
print(salas[2][3][2]) # 20

print()

for sala in salas:
    for aluno in sala:
        print(aluno)