"""
https://docs.python.org/pt-br/3/library/stdtypes.html
Imutáveis que vimos: str, int, float, bool
"""
string = 'Pro Player'
outra_string = f'{string[:2]}ABC {string[4:]}'

print(string)
print(outra_string)

print(string.capitalize()) # Primeira letra maiuscula e as letras restantes minusculas
print(string.zfill(20)) # Preenche o restante com 0's até atingir o valor digitado (Caracteres da variavel contam)