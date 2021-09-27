"""
num1 = input('Digite um número inteiro: ')

if num1.isdigit():

    num1 = int(num1)
    var = num1 % 2

    if var == 0:
        print(f'{num1} é par')
    else:
        print(f'{num1} é ímpar')

else:
    print('Este não é um número inteiro.')
"""

"""
hora = input('Que horas são (0-23)? ')

if hora.isdigit():

    hora = int(hora)

    if hora < 0 or hora > 23:
        print('Digite um horario entre 0 e 23')
    else:
        if hora <= 11:
            print('Bom dia!')

        if hora <= 17:
            print('Boa tarde!')

        if hora <= 23:
            print('Boa noite!')

else:
    print('Por favor, digite um horario entre 0 e 23.')
"""

"""
usuario = input('Qual o seu primeiro nome? ')
tamanho = len(usuario)

if tamanho <= 4:
    print('Seu nome é muito curto.')

elif 5 <= tamanho <= 6:
    print('Seu nome é normal.')

else:
    print('Seu nome é muito longo.')
"""