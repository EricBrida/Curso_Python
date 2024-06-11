nome = 'Eric Brida'
altura = 1.67
peso = 57.5
imc = peso / altura ** 2

# f-strings -> f = Formatação
linha_1 = f'{nome} tem {altura:.2f} de altura'
linha_2 = f'pesa {peso} quilos e seu IMC é'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)