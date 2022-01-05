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