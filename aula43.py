texto = 'Python'

# i = 0
# tamanho_string = len(texto)

# while i < tamanho_string:
#     print(texto[i])

#     i += 1

nova_string = ''

for letra in texto:
    nova_string += f'*{letra}'
    print(letra)

print(f'{nova_string}*')