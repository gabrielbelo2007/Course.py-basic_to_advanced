"""
Tipos de Dados (Primitivos):
str - string = textos 'Assim' "Assim"
int - número inteiro = 123 -456
float - número real/ponto flutuante -10.50 12.60 0.8 (números decimais)
bool - valor booleano/lógico = True/False   10==10 (true) geralmente comparações
se houver qualquer valor sem comparação no 'bool' é avaliado como 'true'
"""

print('Gabriel', type('Gabriel'))
print(10, type(10))
print(25.23, type(25.23))
print(10 == 10, type(10 == 10))
print('L' == 'L', type('L' == 'L'))
print(bool(''))
print(bool(0))
print(bool([]))

print('Gabriel', type('Gabriel'), bool('Gabriel'))
print('10', type('10'), type(int('10')))
print('Gabriel', float('10.9'))
print('10' + str(10))
