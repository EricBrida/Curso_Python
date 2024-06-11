"""
Introdução ás funções (def) em Python
Funções são trechos de código usados para
replicar determinada ação ao longo do seu código.
Elas podem receber valores para parâmetros (argumentos)
e retornar um valor específico.
Por padrão, funções em Python retornam None (nada).
"""

def Print(a, b):
    c = a + b
    c = c ** 2
    print(c)

Print(7, 5)
Print(9, 9)
Print(20, 12)

def saudacao(nome = 'Sem Nome'):
    print(f'Olá, {nome}!!')

saudacao('Eric')
saudacao('Gi')
saudacao()
