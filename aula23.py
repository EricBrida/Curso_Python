# Operador lógico "not"
# Usado para inverter expressões
# not True = False
# not False = True

senha = input('Senha: ')

if not senha:
    print('Digitou Nada')

print(not True) # False
print(not False) # True