"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""

import os

# palavra_secreta = 'Elefante'
# palavra_oculta = ''
# i = 0
# cont = 0
# rodar = True

# for i in range(len(palavra_secreta)):
#     palavra_oculta += '*'

# palavra_formatada = list(palavra_oculta)

# while rodar:

#     letra = input('Digite apenas UMA letra: ')

#     if len(letra) > 1:
#         print('APENAS UMA LETRA...')
#         continue
#     elif letra.isdigit():
#         print('Não pode números')
#         continue

#     for i in range(len(palavra_secreta)):

#         if letra == palavra_secreta[i]:
#             print(f'A letra "{letra}" está na palavra secreta na posição {i}')
#             palavra_formatada[i] = letra

#     print(palavra_formatada)

#     if palavra_formatada == list(palavra_secreta):
#         rodar = False

#     cont += 1

# os.system('cls')
# print(f'A palavra que você conseguiu foi {palavra_formatada}, com um total de {cont} tentativas')
# print(f'A palavra secreta era {palavra_secreta}')
# print()

palavra_secreta = 'elefante'
letra_certa = ''
cont = 0

while True:
    
    print()
    letra = input('Digite apenas UMA letra: ')

    if len(letra) > 1:
        print('Digite apenas UMA letra')
        continue
    elif letra.isdigit():
        print('Não pode números')
        continue

    if letra in palavra_secreta:
        letra_certa += letra

    palavra_formada = ''

    for letra_secreta in palavra_secreta:
        if letra_secreta in letra_certa:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    print(palavra_formada)

    if palavra_formada == palavra_secreta:
        break

    cont += 1

os.system('cls')
print('Você conseguiu')
print(f'Com um total de {cont} tentativas')