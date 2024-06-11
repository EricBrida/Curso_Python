# Exemplo de uso dos sets

letras = set()

while True:

    letra= input('Letra: ')
    letras.add(letra)

    if 'l' in letras:
        print('boa')
        break

    print(letras)

