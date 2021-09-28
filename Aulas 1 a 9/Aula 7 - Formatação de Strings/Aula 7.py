"""
Formatação de Strings (str)
"""

nome = 'Gabriel'  # = é um operador de atribuição
idade = 14  #int
altura = 1.68  #float
e_maior = idade > 18  #bool
peso = 50
imc = peso / altura ** 2

print(nome, 'tem', idade, 'anos de idade e seu imc é', imc)
print(f'{nome} tem {idade} anos de idade e seu imc é {imc}')
print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}')
print('{0} tem {1} anos de idade e seu imc é {2}'.format(nome, idade, imc))
print('{1}{1}{0} tem {1} anos de idade e seu imc é {2}'.format(nome, idade, imc))
print('{n} tem {i} anos de idade e seu imc é {im}'.format(n=nome, i=idade, im=imc))
