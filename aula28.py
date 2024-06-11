# Exercício

nome = input('Digite seu Nome: ')
idade = input('Digite sua Idade: ')

if nome == '' or idade =='':
    print('Desculpe, você deixou campos vazios')
else:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')
    print('Seu nome contém espaços? ', ' ' in nome)
    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é: {nome[0]}')
    print(f'A última letra do seu nome é: {nome[len(nome) - 1]}')