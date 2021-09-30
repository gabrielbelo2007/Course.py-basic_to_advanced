"""
Listas em Python

fatiamento
append, insert, pop, del, clear, extend, +
min, max
range
"""

"""
# Criação de lista: 1. Nome da Variavel 2. Entre colchetes coloque os valores.

lista = [1, 2, 3, 4, "Gabriel Belo", True, 14.6]  # Pode usar qualquer dado

# Índice   0    1         2    3    4   5
l1 = ['A', 'Bacana', 'C', 'D', 'E', 12.5]
# Índice - 6    5         4    3    2    1
l1[5] = 'Qualquer outra coisa'  # Altera o valor de determinado índice

string = 'ABacanaCDE'

print(string[1])
print(l1[5])
print(l1[1:4])  # O número que determina a parada do fatiamento não conta
"""

"""
l2 = [1, 2, 3]
l3 = [4, 5, 6]
l4 = l2 + l3

print(l2)
print(l3)
print(l4)

l2.extend(l3)
print(l2)
l3.append('b')  # Insere um novo valor no final da lista (novo índice)
print(l3)
l3.insert(0, 'banana')  # Insere um novo valor em um determinado índice
print(l3)
l3.pop(2)  # Retira um valor determinado pelo índice
print(l3)
"""

"""
l5 = [1, 2, 3, 4, 5, 6, 7, 8, 10, 10.5,  9]
print(l5)

l5.insert(0, 'nada')
print(l5)

del(l5[3:6])  # Apaga os valores entre os índices determinados
del(l5[0])
print(l5)

print(max(l5))  # Maior valor da lista (se apresentar números, caso contrário maior índice)
print(min(l5))  # Menor valor da lista 
"""

"""
l6 = list(range(0, 100, 8))  # List: converte um objeto iteravel em uma lista
print(l6)

l7 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

soma = 0
for valor in l7:
    soma = soma + valor
    print(f'{soma} + {valor} = {soma}')

l8 = ['String', True, 10, -20.5]

for elem in l8:
    print(f'O tipo de elem é {type(elem)} e seu valor é {elem}')
"""