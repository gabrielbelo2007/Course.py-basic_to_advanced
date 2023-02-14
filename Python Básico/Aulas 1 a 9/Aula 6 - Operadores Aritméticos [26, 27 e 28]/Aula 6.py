"""
Operadores Aritméticos:
+ Adição, pode ser utilizado para unir dois termos (str)
- Subtração
* Multiplicação, pode ser utilizado como repetição
/ Divisão (float)
// Divisão Inteira (int) ou (float), faz o arredondamento da divisão
** Exponenciação
% Resto da Divisão
() Mesmo uso de expressões matematicas
"""

print(10 * 10)
print(10 * '10')
print(10 + 10)
print('5' + '5')
print(10 - 5)
print(10 / 2)
print(10 // 3) #int
print(10.5 // 3) #float
print(2 ** 10)
print(10 % 5)
print(10 % 3)
print(5 + 2 * 10)
print((5 + 2) * 10)


# Precedências dos operadores

# 1. (n + n)
# 2. **
# 3. * / // %
# 4. + -
conta_1 = (1 + int(0.5 + 0.5)) ** (5 + 5)
print(conta_1)


# Concatenação e repetição

concatenacao = 'Luiz' + ' ' + 'Otávio'
print(concatenacao)

a_dez_vezes = 'A' * 10
tres_vezes_luiz = 3 * 'Luiz'
print(a_dez_vezes)
print(tres_vezes_luiz)