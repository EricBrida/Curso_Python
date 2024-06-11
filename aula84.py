# Set
# Métodos úteis:
# add, update, clear, discard

s1 = set()
# s1.add(2)
# s1.add(2)
# s1.add(3)
# s1.update('Olá Mundo') # Vai iterado para o set
# s1.update(('Olá Mundo',1 , 2, 3, 4)) # Itera a tupla
# s1.discard('Olá Mundo') # Tipo um delete

# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos

s1 = {1, 2, 3, 6}
s2 = {3, 4, 5, 6}
s3 = s1 ^ s2
print(s3)