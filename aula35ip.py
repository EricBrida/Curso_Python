contador = 0

while contador <= 100:
    contador += 1
     
    if contador % 2 == 0:
       print(f'{contador} é par')
    else:
        print(f'{contador} é impar')

print('Acabou')