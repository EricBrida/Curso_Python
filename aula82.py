# Exercício - sistema de perguntas e respostas

import os

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

qtd_acertos = 0

for pergunta in perguntas:
    enunciado = list(pergunta.items())
    pergunta_processo = enunciado[0]
    pergunta_str = ': '.join(pergunta_processo)
    print(pergunta_str)

    opcoes = enunciado[1][1]

    for i, opcao in enumerate(opcoes):
        print(i , ') ', opcao)

        if i == 3:
            resposta_dada = input('Resposta: ')

            if resposta_dada == list(enunciado[2]).pop():
                print('Acertou', end='\n\n\n')
                qtd_acertos += 1
            else: print('Errou', end='\n\n\n')


print(f'Você acertou {qtd_acertos} de {len(perguntas)}')