# Crie uma função que exibe uma saudação com os parâmentos 'saudacao' e 'nome'.
"""
def cumprimento(saudacao, nome):
    print(saudacao, nome)

cumprimento('Olá', 'Gabriel')
"""

# Crie uma função que recebe 3 números como parâmetros e exiba a soma entre eles.
"""
def soma(n1, n2, n3):
    print(n1 + n2 + n3)

soma(2, 2, 3)
"""

# Crie uma função que receba 2 números. O primeiro é um valor e o segundo um percentual.
# Retorne o valor do primeiro número somado com o seu percentual.
"""
def aumento(z, y):
    return n1 + (n1 * n2 // 100)

n1 = int(input('Valor: '))
n2 = int(input('Porcentagem do valor: '))
ap = (aumento(n1, n2))
print(ap)
"""


# FizzBuzz - Se o parâmetro da função for divisível por 2, retorne fizz, se o parâmetro da
# função for divisível por 5, retorne buzz. Se o parâmetro da função for divisível por 5 e 3,
# retorne FizzBuzz, caso contrário, retorne o número enviado.


def jogo(n):
    if n % 3 == 0 and n % 5 == 0:
        return 'FizzBuzz'

    elif n % 3 == 0:
        return 'fizz'

    elif n % 5 == 0:
        return 'buzz'

    return f'Esse é o seu numero {n}'

valor = int(input('Valor: '))
print(jogo(valor))

# Detalhe do professor
"""
from random import randint

for i in range(100):
    aleatorio = randint(0, 100)
    print(jogo(aleatorio))
"""