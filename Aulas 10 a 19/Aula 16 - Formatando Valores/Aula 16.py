"""
Formatando Valores

:s - Textos (str)
:d - Inteiros (int)
:f - Ponto Flutuante (float)
:.(numero)f - Quantidade de casas decimais (float)
:(Caractere)(> ou < ou ^)(Quantidade)(Tipo - s, d ou f)

> - esquerda
< - direita
^ - centro
"""

num_1 = 10
num_2 = 3
divisao = num_1 / num_2

print('{:.2f}'.format(divisao))
print(f'{divisao:.2f}')  # f(str) é mais utilizado

nome = 'Gabriel'
print('{:s}'.format(nome))
print(f'{nome:s}')

num_3 = 2
print('{:d}'.format(num_3))
print(f'{num_3:d}')


num_4 = 1
print(f'{num_4:0>10}')  # a variavel tem que ter 10 casas contando com o número principal

num_5 = 1150
print(f'{num_5:0<10}')

num_6 = 22
print(f'{num_6:0^10}')

num_7 = 45
print(f'{num_7:.3f}')

nome_1 = 'Gabriel'
sobrenome = 'Belo'
nome_formatado = '{0} {1:#^50}'.format(nome_1, sobrenome)
print(f'{nome_1:#^50}')
print(nome_formatado)

print(nome_1.lower())  # Tudo minusculo
print(nome_1.upper())  # Tudo maiusculo
print(nome_1, sobrenome.title())  # Primeiras letras de cada string maisculas


