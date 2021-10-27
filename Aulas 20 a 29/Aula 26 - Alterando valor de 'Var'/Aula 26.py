"""
Trocando o valor entre variaveis
"""

x = 10  # Queremos trocar por 'Gabriel'
y = 'Gabriel'  # Queremos trocar por 10
z = 'Belo'

'''
# Uma maneira de fazer (muito obsoleta):

z = x  # Poderia ser 'y'
x = y 
y = z

print(f'O valor de X = {x} e o de Y = {y}')
'''

# Maneira pratica de fazer no Python

z, y, x = y, x, z  # z ta recebendo o valor de y, y o valor de x, x o valor de z
print(f'O valor de X = {x}, o de Y = {y} e o de Z = {z}')