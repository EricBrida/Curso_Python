import importlib

import aula104m

print(aula104m.variavel)

for i in range(10):
    print(i)
    importlib.reload(aula104m)

print('Fim')