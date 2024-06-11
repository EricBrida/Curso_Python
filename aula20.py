primeiro_numero = input('Digite um valor: ')
segundo_numero = input('Digite outro valor: ')

if primeiro_numero > segundo_numero:
    print(f'{primeiro_numero=} é maior que o {segundo_numero=}')
elif segundo_numero > primeiro_numero:
    print(f'{segundo_numero=} é maior que o {primeiro_numero=}')
else:
    print(f'Os números {primeiro_numero=} e {segundo_numero=} são iguais')