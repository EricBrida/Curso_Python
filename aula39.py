"""
Iterando strings com while
"""

nome = input('Digite seu nome: ') # Eric
tamanho_nome = len(nome)
nova_string = '*'
contador = 0

# while contador < tamanho_nome:
#     print(nome[contador])      # -> Cada linha mostra uma letra em sequência
#     contador += 1

while contador < tamanho_nome:
    nova_string += f'{nome[contador]}*'
    contador += 1

print(nova_string) # *E*r*i*c