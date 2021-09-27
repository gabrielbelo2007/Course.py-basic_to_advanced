"""
Operadores Lógicos (Valores Bool)
and, or, not
in e not in
"""

# comparação_1 AND comparação_2 (caso as duas sejam verdadeiras) = True
# comparação_1 AND comparação_2 (se UMA for falsa) = False
# comparação_1 OR comparação_2 (apenas uma precisa ser verdadeira) = True
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
