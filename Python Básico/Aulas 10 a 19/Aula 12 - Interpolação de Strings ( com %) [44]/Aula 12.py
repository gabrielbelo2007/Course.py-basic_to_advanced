"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
x = Hexadecimal minúsculo  e  X = Hexadecimal Maiúsculo

As variáveis devem ser colocadas na ordem em que aparecem
"""

nome = 'Luiz'
preco = 1000.95897643
variavel = '%s, o preço é R$%.2f' % (nome, preco)  # Só é necessario os parenteses se tiver mais de um valor
variavel1 = 'Meu nome é %s' % nome

print(variavel)
print(variavel1)
print('O hexadecimal de %d é %08X' % (1500, 1500))
