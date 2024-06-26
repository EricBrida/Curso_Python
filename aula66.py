"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""

import random

for j in range(100):

    cpf = []

    for i in range(9):
        cpf.append(random.randint(0, 9))

    numero_multiplicacao = 10
    soma = 0

    for i, num in enumerate(cpf):
        soma += (num * numero_multiplicacao)
        numero_multiplicacao -= 1

    primeiro_digito = (soma * 10) % 11
    primeiro_digito = primeiro_digito if primeiro_digito <= 9 else 0

    cpf.append(primeiro_digito)

    soma = 0
    numero_multiplicacao = 11

    for i, num in enumerate(cpf):
        soma += (num * numero_multiplicacao)
        numero_multiplicacao -= 1

    segundo_digito = (soma * 10) % 11
    segundo_digito = segundo_digito if segundo_digito <= 9 else 0

    cpf.append(segundo_digito)
    cpf_str = ' '.join(str(cpf).strip('[]').split( ))
    cpf_str_formatado = cpf_str.replace(',', '').replace(' ', '')
    print(cpf_str_formatado)
