""" 
args - Argumentos não nomeados
*_ == *args(conveção para simbolizar argumentos inumerados) - dempacotamento e desempacotamento
"""

# Empacotamento (já visto)
x, y, *resto = 1, 2, 3, 4
print(x, y, resto)

def soma(*args):  # Esse empacotamento retorna um type(): tupla
    total = 0
    for numero in args:
        total += numero
        print(numero, total)
    
soma(1, 2, 3, 4, 5, 6)

numeros = 1, 2, 3, 4, 5, 6, 80  # Esse valor é uma tupla
outra_soma = soma(*numeros)  # É necessário desempacotar pois a função: soma, empacota a tupla: números, fica uma tupla dentro de outra
