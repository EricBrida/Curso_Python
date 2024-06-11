# groupby -> agrupando valores (itertools)

from itertools import groupby

def ordena(aluno):
    return aluno['nota']

alunos = [

    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},

]

# alunos = ['a', 'a', 'a', 'a', 'b', 'c']
# grupos = groupby(alunos)

# for chave, grupo in grupos:
#     print(chave)
#     print(list(grupo))

alunos_agrupados = sorted(alunos, key=ordena)
grupos = groupby(alunos_agrupados, key=ordena)

for chave, grupo in grupos:
    print(chave)
    
    for aluno in grupo:
        print(aluno)

print(end='\n\n\n')

for grupo in alunos_agrupados:
    print(grupo)