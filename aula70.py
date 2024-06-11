"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançavel
O escopo local é o escopo onde apenas nomes do mesmo local
pode sem alcançados.
"""

x = 1

def escopo(): # Cria outra CallStack para executar a função escopo.

    x = 5

    def outra_funcao():

        x = 11
        y = 34

        print(x, y)

    outra_funcao()
    print(x)

print(x)
escopo()
print(x)