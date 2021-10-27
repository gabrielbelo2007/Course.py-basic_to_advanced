"""
Expressão Condicional com o operador OR
"""

nome = input('Qual seu nome? ')

'''
# Uma maneira de fazer (Mais obsoleta)
if nome:
    print(f'O seu nome é {nome}.')
else:
    print('Você não digitou nada.')
'''

# Mesmo resultado da anterior:
print(nome or 0 or False or "Você não digitou nada!")
# OR = Ele vai ler as expressões ignorar as Falses e parar
# Assim que achar a primeira que for True, nesse caso a ultima str.
# Ele ignora outras variaveis que aparecerem após a primeira que ele achou True