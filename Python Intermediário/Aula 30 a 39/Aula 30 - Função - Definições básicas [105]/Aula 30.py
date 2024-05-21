"""
Funções são trechos de código usados para replicar ações ao longo do código.
Executados por parênteses e caso necessário, com . -> funcao(argumento)

Elas podem receber argumentos para seus parâmetros (variaveis) e retornar um valor específico.
Por padrão, funções no Python retornam None (== False em Bool).
"""


def imprimir(a, b, c):
    print(a, b, c)

imprimir(1, 2, 3)  # Prencher todos os argumentos -> a = 1, b = 2, c = 3


def saudacao(nome):
    print(f"Oi, {nome}!")

saudacao("Bel")  # Executa o codigo da funcao e atribui o parametro
saudacao("Gab")


"""
Argumentos nomeados e nao nomeados em funcoes no Python

Argumento nomeado tem nome com sinal de igual -> (nome = "Gabriel")
Argumento nao nomeado recebe apenas o argumento -> (valor)
"""

def soma(x, y, z):
    print(f"{x=} y={y} {z=}", "I", "x + y + z = ", x + y + z)

soma(1, 2, 3)  # Atribui os argumentos na ordem que sao posicionados
soma(y=2, x=1, z=3)  # Determina onde atribuir cada argumento

# soma(1, y=2, 3) -> Erro
# Todos que vierem depois do argumento nomeado precisam ser nomeados


""" 
Valores padrão para parâmetros:

Ao definir uma função, os parâmertros podem ter valores padrão.
Caso o valor não tenha argumento para o parâmetro, o valor padrão vai ser usado.

Utilizador para refatorar (editar códigos "prontos") código.
"""

def soma(x,y, z=None):
    if z is not None:
        print(f"{x=} {y=} {z=}", x + y + z)
    else:
        print(f"{x=} {y=}", x + y)
        
soma(1, 2)
soma(1, 2, 3)
soma(y=9, z=0, x=7)


""" 
Retorno de valores das funções - return
return -> Atribui um valor para a função e quebra sua execução
"""

def soma(x, y):
    return x + y
#   print(1+1) -> Depois do "return" nada pode ser executado na função

soma1 = soma(2, 3)  # A função soma() retorna o valor de x + y, podendo atribuir esse valor a uma variável
soma2 = soma(3, 3)

print(soma1 + soma2)
