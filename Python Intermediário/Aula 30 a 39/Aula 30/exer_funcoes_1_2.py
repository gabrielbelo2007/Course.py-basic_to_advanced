"""
1 - Crie uma função que exibe uma saudação com os parâmetros saudacao e nome.
"""

# def saudacao(saudacao, nome):
#     print(f'{saudacao} {nome}')
#
# saudacao('Olá', 'Joãozinho')
# saudacao('Oi', 'Maria')
# saudacao('Hey', 'Eduardo')


"""
2 - Crie uma função que recebe 3 números como parâmetros e exiba a soma entre 
eles.
"""

# def soma(n1, n2, n3):
#     print(n1 + n2 + n3)
#
#
# soma(2, 1, 3)
# soma(1, 1, 1)
# soma(2, 1, 1)

"""
3 - Crie uma função que receba 2 números. O primeiro é um valor e o segundo um
percentual (ex. 10%). Retorne (return) o valor do primeiro número somado
do aumento do percentual do mesmo.
"""

# def aumento_percentual(valor, percentual):
#     return valor + (valor * percentual / 100)
#
#
# ap = aumento_percentual(50, 10)
# print(ap)
# ap = aumento_percentual(100, 10)
# print(ap)
# ap = aumento_percentual(10, 10)
# print(ap)
# ap = aumento_percentual(15, 100)
# print(ap)


"""
4 - Fizz Buzz - Se o parâmetro da função for divisível por 3, retorne fizz,
se o parâmetro da função for divisível por 5, retorne buzz. Se o parâmetro da
função for divisível por 5 e por 3, retorne FizzBuzz, caso contrário, retorne o
número enviado.
"""


# def fb(n):
#     if n % 3 == 0 and n % 5 == 0:
#         return f'fizzbuzz, {n} é divisível por 3 e 5'
#     if n % 5 == 0:
#         return f'buzz, {n} é divisível por 5'
#     if n % 3 == 0:
#         return f'fizz, {n} é divisível por 3'
#     return n
#
#
# from random import randint
#
# for i in range(100):
#     aleatorio = randint(0, 100)
#     print(fb(aleatorio))
