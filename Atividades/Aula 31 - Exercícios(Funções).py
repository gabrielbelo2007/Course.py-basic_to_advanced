"""
def func1():
    return 'Hello World!'


def func2(funcao):
    return funcao()

executar = func2(func1)
print(executar)
"""


def func1(funcao, funcao1):
    return funcao(), funcao1()


def func2(*args):
    return 10, 20


def func3(*args):
    return 10, 20, 30


executar = func1(func2, func3)
print(executar)


"""
Professor:

def mestre(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)


def fala_oi(nome):
    return f'Oi {nome}'


def saudacao(nome, saudacao):
    return f'{saudacao} {nome}'


executando = mestre(fala_oi, 'Luiz')
executando2 = mestre(saudacao, 'Luiz', saudacao='Bom dia!')
print(executando)
print(executando2)
"""