"""
Operador ternário
"""

logged_user = False

'''
# Uma maneira de fazer (Mais obsoleta)
if logged_user:
    msg = 'Usuário Logado'
else:
    msg = 'Usuário precisa logar'

print(msg)
'''

# Mesmo resultado da anterior:

msg = 'Usuário Logado' \
    if logged_user else 'Usuário precisa logar'
print(msg)

# msg = é uma variavel que vai mudar dependendo de uma condição, por isso para encurtar
# como a condição altera o seu valor, basta adicionar as condições na mesma linha da variavel
# pode usar uma barra invertida para dizer que as condições pertencem a linha da variavel

idade = input('Qual a sua idade? ')

if not idade.isnumeric():
    print('Você precisa digitar um número!')
else:
    idade = int(idade)
    eh_maior = (idade >= 18)
    msg = 'Pode acessar, bem vindo!' if eh_maior else 'Não pode acessar.'
    print(msg)

