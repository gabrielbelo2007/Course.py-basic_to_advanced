"""
Entrada de Dados - Aula 3 - Strings
"""


nome = input("Qual o seu nome? ")  # sempre retorna o valor no formato str
idade = input("Qual a sua idade? ")
ano_nascimento = 2021 - int(idade)


print()  # apenas para quebra de linha
print(f'O usuario digitou {nome} e o tipo de variavel é', f'{type(nome)}')
print(f'{nome} tem {idade} anos.')
print(f'Logo nasceu em {ano_nascimento}')
print()

# 3 formas diferentes formas de alterar o type
numero_1 = int(input('Digite um número: '))  # 1 forma

numero_2 = input('Digite um número: ')
numero_2 = int(numero_2)  # 2 forma (melhor forma)

print('resultado: ', int(numero_1) + int(numero_2))  # 3 forma
print('resultado: ', int(numero_1) ** int(numero_2))
