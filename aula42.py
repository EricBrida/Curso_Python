# Exercício
# Qual letra mais apareceu na frase
# .count() -> Conta quantos caracteres apareceram em uma string

frase = 'Python é uma linguagem de programação multiparadigma. Python foi criado por Guido van Rossum.'.lower()
i = 0
j = 0
contador = 0
maior = 0
letra_maior = ''

while i < len(frase):
    
    letra = frase[i]

    while j < len(frase):

        if letra == ' ':
            ...
        elif letra == frase[j]:
            contador += 1

        j += 1

    if contador > maior:
        maior = contador
        letra_maior = letra

    i += 1
    contador = 0
    j = 0

string = f'A letra que mais apareceu foi "{letra_maior.upper()}", aparecendo um total de {maior} vezes'
print(string)
    

