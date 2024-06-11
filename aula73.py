# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

import random
import os

def multiplicacao(*args):
    total = 1

    for num in args:
        total *= num

    return total

numeros = []

for i in range(5):
    numeros.append(random.randint(1, 9))

print(numeros)

resultado = multiplicacao(*numeros)
print(resultado)

input()
os.system('cls')

# Crie uma função que fale se o número é par ou impar

def par_impar(teste):
    
    if teste % 2 == 0:
        return 'Par'

    return 'Impar'



num = random.randint(0, 9999)

print(f'Numero escolhido -> {num}')
par_impar_str = par_impar(num)
print(par_impar_str)
input()