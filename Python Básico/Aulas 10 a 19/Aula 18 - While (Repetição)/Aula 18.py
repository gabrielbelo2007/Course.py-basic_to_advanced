"""
While (estrutura de repetição) em Python

Utilizado para realizar ações ENQUANTO uma condição for verdadeira.

Requisitos: Entender condições e operadores
"""


x = 0
while x < 10:  # loop infinito, while executa o bloco enquanto a condição for verdadeira.
    if x == 3:
        x = x + 1
        continue  # ignora o proximo bloco de comando ou volta para o inicio
        # caso o o bloco anterior não possa ser executado novamente ele prossegue normal

    if x == 8:
        break  # encerra qualquer código mesmo que a condição permaneça True

    print(x)
    x = x + 1

print('Acabou!')  # só sera executado quando 'while' for False.


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

