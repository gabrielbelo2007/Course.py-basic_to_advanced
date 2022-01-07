"""
Funções: def

def = Voce define uma função, escolhendo o seu nome e sua ação (sem limites de códigos)

Entre os parenteses pode ser colocado uma variavel, e seu valor pode ser alterado
em cada execução da função.

Os valores das variaveis podem ser colocado na definição da função, sendo assim quando
ocorrer a execução, sem nada entre os parenteses, serão esses valores que vão aparecer.

OBS: Sem utilização dos parenteses em uma função, ela não é executada.
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