nome = 'Gabriel'
idade = 14
altura = 1.68
e_maior = idade > 18
peso = 50
imc = peso / altura ** 2
ano = 2021
nascimento = ano - idade


print(f'{nome} tem {idade} anos, {altura} de altura e pesa {peso} kg.')
print(f'O IMC de {nome} é {imc:.2f}.')
print(f'{nome} nasceu em {nascimento}.')

