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


# Coerção de tipos

# type conversion, typecasting, coercion
# é o ato de converter um tipo em outro
#  tipos imutáveis e primitivos:
# str, int, float, bool
print(int('1'), type(int('1')))
print(type(float('1') + 1))
print(bool(' '))
print(str(11) + 'b')
