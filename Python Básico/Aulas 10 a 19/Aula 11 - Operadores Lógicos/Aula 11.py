"""
Operadores Lógicos (Valores Bool)
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser
# verdadeiras.
# Se qualquer valor for considerado falso,
# a expressão inteira será avaliada naquele valor
# São considerados falsy (que vc já viu)
# 0 0.0 '' False
# Também existe o tipo None que é
# usado para representar um não valor
"""

# comparação_1 AND comparação_2 (caso às duas sejam verdadeiras) = True
# comparação_1 AND comparação_2 (se UMA for falsa) = False
# comparação_3 OR comparação_4 (apenas uma precisa ser verdadeira) = True
# NOT a > b (funciona como um inversor do resultado, ia ser true) = False

a = 2
b = 2
c = 3

var = a == b and b < c
var_1 = a == b or b < c
var_2 = not a == b, not b < c
print(var)
print(var_1)
print(var_2)

nome = 'Gabriel'
if 'a' in nome:
    print('Existe.')
else:
    print('Não existe.')

if 'u' not in nome:
    print('Não existe.')

if 'a' not in nome:
    print('Não Existe.')
else:
    print('Existe.')

usuario = input('Nome de usuario: ')
senha = input('Senha de usuario: ')

senha = int(senha)
usuario_bd = 'Gabriel'
senha_bd = 1234

if usuario == usuario_bd and senha == senha_bd:
    print('Você está logado no sistema')
else:
    print('Você não está logado no sistema')
