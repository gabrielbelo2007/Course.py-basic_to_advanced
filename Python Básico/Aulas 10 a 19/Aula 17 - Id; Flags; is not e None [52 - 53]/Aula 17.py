"""
Flag (Bandeira) - Marcar um local
None = Não valor
is e is not = é ou não é (tipo, valor, identidade)
id - Identidade
"""

# As duas variaveis estao apontando para o mesmo valor na memoria
v1 = "a"
v2 = "a"
print(id(v1))
print(id(v2))

condicao = False
passou_no_if = None

if condicao:
    passou_no_if = True  # Flag - Verifica se o codigo dentro desse if esta sendo lido
    print('Faca algo')
else:
    print('Nao faca algo')

print(passou_no_if, passou_no_if is None)
print(passou_no_if, passou_no_if is not None)
