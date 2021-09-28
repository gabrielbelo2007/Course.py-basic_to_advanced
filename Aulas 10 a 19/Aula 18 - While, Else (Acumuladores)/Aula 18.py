"""
While (estrutura de repetição) em Python

Utilizado para realizar ações ENQUANTO uma condição for verdadeira.

Requisitos: Entender condições e operadores
"""

"""
x = 0
while x < 10:  # loop infinito, while executa o bloco enquanto a condição for verdadeira.
    if x == 3:
        x = x + 1
        continue  # ignora o proximo bloco de comando

    if x == 8:
        break  # encerra o comando while mesmo que a condição permaneça True

    print(x)
    x = x + 1

print('Acabou!')  # só sera executado quando 'while' for False.
"""

"""
x = 0  # coluna

while x < 10:
    y = 0  # linha

    while y < 5:
        print(f'X vale {x} e Y vale {y}. ')
        y += 1

    x += 1  # x = x + 1

print('Acabou!')
"""

while True:
    print()
    num_1 = input("Digite um numero: ")
    num_2 = input("Digite outro numero: ")
    operador = input('Digite um operador: ')
    sair = input('Deseja Sair? [s]im ou [n]ão: ')

    if sair == 's':
        break

    # operadores: + - / *

    if not num_1.isdigit() or not num_2.isdigit():
        print('Voce precisa digitar um número.')
        continue

    num_1 = int(num_1)
    num_2 = int(num_2)

    if operador == '+':
        print(num_1 + num_2)
    elif operador == '-':
        print(num_1 - num_2)
    elif operador == '/':
        print(num_1 / num_2)
    elif operador == '*':
        print(num_1 * num_2)
    else:
        print('Operador invalido')