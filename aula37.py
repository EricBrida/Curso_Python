"""
Repetições
while -> Enquanto
Executa uma ação enquanto uma condição for verdadeira
Loop Infinito -> Quando um código não tem fim
"""

contador = 0

while contador <= 1000:
    contador += 1

    if contador % 2 == 0: # Pula números pares / Ao se deparar com continue, retorna ao começo do while
        continue

    print(contador)

print('Acabou')

