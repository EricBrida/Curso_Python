# Entendendo seus próprios módulos Python
# O primeiro módulo executado chama-se __main__
# Você pode importar outro módulo inteiro ou parte de módulo
# O Python conhece a pasta onde o __main__ está e as pastas
# Abaixo dele
# Ele não reconhece pastas e módulos acima do __main__ por
# Padrão
# O Python conhece todos os módulos e pacotes presentes
# nos caminhos de sys.path

import aula103m

from aula103m import num as numero

print('Este arquivo é o: ', __name__)
print(numero, aula103m.res)

print(aula103m.soma(1, 2))
