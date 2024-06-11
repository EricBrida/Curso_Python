# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']

import json

def checa_input(parametro):

    if parametro == 'lista':
        return lista()
    if parametro == 'desfazer':
        return desfazer(desfaz)
    if parametro == 'refazer':
        return refazer(desfaz)
    if parametro == 'sair':
        return exit()

    
    return insere(parametro)

def ler_json():
    dados = []
    with open('aula125.json', 'r', encoding='utf-8') as caminho_arquivo:
        dados = json.load(caminho_arquivo)
    
    return dados

def insere(parametro):

    fazeres.append(parametro)
    for i in fazeres:
        print(i)

def lista():
    for i, fazer in enumerate(fazeres):
        print(f'{i + 1}º -> {fazer}')

    print(end='\n\n')

def desfazer(desfaz):

    if len(fazeres) == 0:
        print('Não há nada a desfazer')
        return

    if desfaz is None:
        desfaz = []

    desfaz.append(fazeres.pop())
    

def refazer(desfaz):

    if len(desfaz) == 0:
        print('Não há nada a refazer')
        return
    
    fazeres.append(desfaz.pop())

fazeres = ler_json()
desfaz = []

try:
    while(True):

        print('Comandos: lista, refazer, desfazer, sair')
        coisa = input('Digite uma tarefa ou comando: ')
        print(end='\n\n')
        print('TAREFAS', end='\n\n')
        checa_input(coisa)

finally:
    with open('aula125.json', 'w', encoding='utf-8') as arquivo:
        json.dump(fazeres, arquivo)