"""
Funções (def): *args, **kwargs

Não obrigatoriamente precisa ser colocado "args" ou "kwargs" isso é mais um padrão,
porém só é necessario os astéricos.
"""

"""
def func(*args):
    for v in args:
        print(args)
    print(args[0])
    print(len(args))

func(1, 2, 3, 4, 5)


# Args é uma tuple possuindo comandos que usamos na lista e podem virar listas
lista = [1, 2, 3, 4, 5]
n1, n2, *n = lista  # Desempacotou 2 valores e "guardou o resto"
print(n1, n2, n)

lista = [6, 7, 8, 9]
print(*lista, sep='-')
"""

"""
def func1(*args, **kwargs):
    print(args)
    print(kwargs)  # Mostra os argumentos com valores determinados (args não mostra)


lista1 = [1, 2, 3, 4, 5]
lista2 = [10, 20, 30, 40, 50]
func1(*lista1, *lista2, nome='Gabriel', sobrenome="Belo")
# As listas foram desempacotadas formando uma tuple
"""

# Melhor forma de se usar "kwargs", para não apresentar erros no código, quando não se tem
# certeza sobre os argumentos do código


def func2(**kwargs):

    idade = kwargs.get('idade')

    if idade is not None:
        print(f'Sua idade é {idade} anos')

    altura = kwargs.get('altura')

    if altura is not None:
        print(altura)

    else:
        print('Não foi enviado os dados de altura')

func2(idade=14)
