# Funções Anônimas (Não possuem nomes)
# Funções colocadas dentro de variaveis, de maneira mais simples que o 'def.', para facilitar
# o uso de funcs como parâmetros

def funcao(arg, arg2):
    return arg * arg2


var = funcao(2, 2)
print(var)

# Mesma função de:

a = lambda x, y: x * y
print(a(2, 2))


# Formas de utilização:

lista = [
    ['P1', 12],
    ['P2', 6],
    ['P3', 7],
    ['P4', 50],
    ['P5', 8],
]


def func(item):
    return item[1]

lista.sort(key=func, reverse=True)  # Altera a lista original
# Função para ordenar uma lista, nesse caso ordenando pelo preço, já que o primeiro parâmetro da
# lista é um número, ordenou do maior para o menor, utilizando o 'reverse' ocorre o inverso
print(lista)

# Essa função utilizada para ordenar tem o mesmo valor de usar (lambda):

"""
lista.sort(key=lambda item: item[1])
print(lista)
"""

print(sorted(lista, key=lambda i: i[1]))  # Ordena a lista sem alterar a original
print(lista)
