# add (adiciona), update (atualiza), clear, discard
# union (une)
# intersection E (todos os elementos presentes nos dois sets)
# difference - (elementos apenas no set da esquerda)
# symmetric_difference ^ (Elementos que estão nos dois sets, mas não em ambos)

# IMPORTANTE: Sets não respeitam ordem na iteração

s1 = {1, 2, 3, 4, 5}  # Não possui indice, embora possa ser iterado
print(s1)

for v in s1:
    print(v)

s2 = {}  # Dicionario
s3 = set()  # Set vazio
s3.add(1)  # Adicionando um valor ao set
s3.add(2)
s3.discard(2)  # Remove o elemento nos parenteses caso ele exista no set
print(type(s2))
print(s3, type(s3))

s4 = set()
s4.update('olá')  # Adiciona o elemento, porém de maneira iterada
s4.update([1, 2, 3, 4, 5], {5, 6, 7, 8})  # Não repete valores iguais
print(s4)

# Serve para remover elementos duplicados em uma lista

l1 = [1, 2, 1, 1, 1, 3, 3, 3, 4, 4, 'olá', 'olá']
l1 = set(l1)  # Retira as duplicatas
l1 = list(l1)  # Lista sem duplicatas, porém fora de ordem

# Usando funções nos sets

s5 = {1, 2, 3, 4, 5, }
s6 = {1, 2, 3, 4, 5, 6}
s7 = s5.union(s6)  # Une os dois sets
print(s7)

s7 = s5.intersection(s6)  # Intersecção dos dois sets
print(s7)

s7 = s6 - s5  # Retira o que estiver igual no set da esquerda
print(s7)

s7 = s5 ^ s6  # Mostra apenas os valores que são unicos de cada set

# Uso dos sets

l2 = ['Sonia', 'Isabel', 'Gabriel']
l3 = ['Sonia', 'Isabel', 'Gabriel', 'Sonia', 'Isabel', 'Gabriel',
      'Sonia', 'Isabel', 'Gabriel']

if set(l2) == set(l3):  # Dessa forma não tira a ordem da lista, mas verifica da mesma forma
    print('l2 é igual a l3')
else:
    print('l2 não é igual a l3')
