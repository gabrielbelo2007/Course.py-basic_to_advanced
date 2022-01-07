"""
Funções: (def) - return

OBS: Funções podem retornar 'tuple', que são listas que não podem ser alterada.
"""

"""
# Para que a função retorne algum valor, utilizamos o "return", com qualquer valor desejado.

def funcao1(var1):
    return var1  # Depois dessa função, nada mais será executado no laço 'def'

variavel1 = funcao1('Valor que eu quero')

if variavel1:
    print(variavel1)
else:
    print('A variavel não possui valor')

"""

"""
def divisao(n1, n2):
    if n2 == 0:  # Evitar que ocorra o "erro de incapaz de dividir por 0"
        return

    return n1 / n2  # Vai ser executado pois o "return" anterior esta dentro do "if"

divide = divisao(8, 2)

if divide:
    print(divide)
else:
    print('Conta inválida')
"""

"""
# Uma função que retorna outra função (não é muito usual, apenas didático)

def f(var):
    print(var)

def dumb():
    return f  # Essa função esta retornando outra função, porém uma função 'desativada'

var = dumb()('O valor da função de F')

if var == f:
    print('Ambos valores são idênticos')
"""


