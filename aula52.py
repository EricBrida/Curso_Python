"""
Cuidados com dados mutáveis
= - copiando valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""

lista_a = ['Maria', 'Jose']
lista_b = lista_a.copy() # Não aponta para o valor da memória

lista_a[0] = 'Qualquer coisa'
print(lista_b)