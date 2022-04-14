"""
def func1():
    return 'Hello World!'


def func2(funcao):
    return funcao()

executar = func2(func1)
print(executar)
"""


def func3(**kwargs):

    nome = kwargs.get('nome')
    if nome is not None:
        print(f'Seu nome é {nome}')


def func4(**kwargs):

    nome = kwargs.get('nome')

    saudacao = kwargs.get('saudacao')
    if saudacao is not None:
        print(f'{saudacao} {nome}')

func3(nome="gabriel")
func4(nome='victor', saudacao='Olá')


def master(funcao1):
    return funcao1()

execute = master(func3)
print(execute)