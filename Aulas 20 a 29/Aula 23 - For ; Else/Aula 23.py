"""
For / Else
"""

"""
variavel = ['Gabriel', 'Azevedo', 'Belo', 'João']

for valor in variavel:
    if valor.lower().startswith('j'):
        # essa função analisa o primeira caractere de um valor
        break
    print(valor)
    
# Lembrando que o python diferencia letra maiúscula de minuscula, a função lower
# Pode se utilizar a função inversa 'upper' alterando a letra a ser analisada

else:  # É executado quando o laço 'for' termina 
    print('Não existe uma palavra que começa com J.')
"""

variavel1 = ['Pedro', 'Henrique', 'Joãozinho']

for valor1 in variavel1:
    if valor1.upper().startswith('J'):
        print('Uma palavra começa com J')
        break
    print(valor1)
else:
    print('Nenhuma palavra começa com J')

# Esse codigo faz a mesma função do anterior



