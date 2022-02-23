"""
Funções: def

def = Voce define uma função, escolhendo o seu nome e sua ação (sem limites de códigos)

Entre os parenteses pode ser colocado uma variavel, e seu valor pode ser alterado
em cada execução da função.

Os valores das variaveis podem ser colocado na definição da função, assim quando
ocorrer a execução, sem nada entre os parenteses, serão esses valores que vão aparecer.

OBS: sem utilização dos parenteses em uma função, ela não é executada.
"""


def saudacao(msg='Olá', nome='Gabriel Belo'):
    nome = nome.replace('e', '3')
    msg = msg.replace('O', '4')
    print(msg, nome)

# .replace = altera o valor de algum elemento de uma var, determinado pela primeira string,
# pelo valor da segunda string

saudacao()
saudacao(nome='zezinho', msg='Bom dia')
saudacao('Oi', 'Lucas')
saudacao('Olá', input('Qual seu nome? '))

"""
def funcao(var):
    print(var)

variavel = funcao('Valor que eu quiser')
print(variavel)  # O valor retornado é "none" que representa um "não valor", false em bool.

if variavel:
    print(variavel)
else:
    print('A variavel não possui valor')
"""

"""
def func(a1, a2, a3, a4, a5, nome=None, a6=None):
    print(a1, a2, a3, a4, a5, nome, a6)

# A partir de um argumento com um valor determinado, todos que vierem depois dele precisam ter 
# seu valor determinado
"""