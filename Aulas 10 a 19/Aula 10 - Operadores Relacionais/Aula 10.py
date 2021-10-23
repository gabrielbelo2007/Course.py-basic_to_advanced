"""
Operadores Relacionais
== > >= < <= !=
"""

num_1 = 2  # pode utilizar nomes
num_2 = '2'
num_3 = 3

expressao = (num_1 == num_3)

print(expressao)
print(num_1 == num_2)
print(2 == 2)  # dois sinais de igual indica pergunta
print(num_1 > num_3)
print(num_1 >= num_3)
print(num_1 < num_3)
print(num_1 <= num_3)
print(num_1 != num_3)  # 'True' se as variaveis forem diferentes

'''
nome = input('Qual o seu nome? ')
idade = int(input('Qual a sua idade? '))

# Limite para pegar emprestimo
idade_limite = 18

if idade >= idade_limite:
    print(f'{nome} pode pegar um emprestimo')
else:
    print(f'{nome} NÃO pode pegar um emprestimo')
'''

nome = input('Qual o seu nome? ')
idade = input('Qual a sua idade? ')

idade = int(idade)

idade_menor = 20
idade_maior = 30

if idade_menor <= idade <= idade_maior:
    print(f'{nome} pode pegar um emprestimo')
else:
    print(f'{nome} NÃO pode pegar um emprestimo')