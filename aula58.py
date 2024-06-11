"""
Faça uma lista de compras com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre 
com erros de índices inexistentes na lista
"""

import os

lista = []

while True:

    print('LISTA DE COMPRAS')
    print('1 - Inserir Items')
    print('2 - Apagar Items')
    print('3 - Listar Items')
    print('4 - Limpar a lista')
    print('5 - Sair')
    opcao = input('Opção: ')

    try:

        opcao_int = int(opcao)

        if opcao_int == 1:
            inserir = input('Qual item deseja inserir na Lista: ')
            lista.append(inserir)
        elif opcao_int == 2:
            apagar = input('Qual item deseja apagar na Lista: ')
            
            for i, compra in enumerate(lista):
                
                if apagar == compra:
                    lista.pop(i)
        elif opcao_int == 3:
            os.system('cls')

            for i, compra in enumerate(lista):
                print(i, compra)
        elif opcao_int == 4:
            lista.clear()
        elif opcao_int == 5:
            print('Saindo...')
            break
        else:
            print('Opção inválida, Por favor tente novamente...')
            continue

    except:
        print('Ocorreu algum erro durante o código, tente novamente')
        continue