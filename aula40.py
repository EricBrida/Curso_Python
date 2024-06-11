# Calculadora com while

rodar = True

while rodar:

    num1 = input('Digite o primeiro número: ')
    num2 = input('Digite o segundo número: ')
    num1_float = 0
    num2_float = 0

    try:
        num1_float = float(num1)
        num2_float = float(num2)
    except:
        print('Valores inseridos não são digitos')
        continue

    operacao = input('Soma (+) | Subtração (-) | Divisão (/) | Multiplicação (*): ')

    if len(operacao) > 1:
        print('Apenas uma operação deve ser feita')
        continue

    if operacao == '+':
        print(f'A soma entre os números {num1_float} e {num2_float} é: {num1_float + num2_float}')
    elif operacao == '-':
        print(f'A subtração entre os números {num1_float} e {num2_float} é: {num1_float - num2_float}')
    elif operacao == '/':
        print(f'A divisão entre os números {num1_float} e {num2_float} é: {num1_float / num2_float}')
    elif operacao == '*':
        print(f'A multiplicação entre os números {num1_float} e {num2_float} é: {num1_float * num2_float}')
    else:
        print('Operador digitado não reconhecido...')
        continue

    sair = input('Deseja sair? [S]im ').upper()

    if sair == 'S': rodar = False

print('Fim do Programa')