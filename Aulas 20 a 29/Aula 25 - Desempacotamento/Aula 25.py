"""
Desempacotamento de Listas
"""

lista_1 = ['João', 'Maria', 'Pedro']

n1, n2, n3 = lista_1
# As variaveis 'n' foram ligadas aos indices do valores da lista, ou seja
# n1 = Indice 0 = João    e assim por diante

print(n1)

# Quando usar o desempacotamento é necessario criar uma variavel para cada indice
# Caso contrario será apresentado um erro, caso não seja necessario para o seu objetivo
# Todos os valores da lista, após desempacotar os necessários use *(crie uma variavel)
# dessa forma será gerado uma lista com os restantes do valor

lista_2 = ['Gio', 'Gabi', 'Nanda', 'Paulo', 'Nat', 'José']

n4, n5, *resto_valor, penultimo_valor, ultimo_valor = lista_2

print(n4, n5, resto_valor, penultimo_valor, ultimo_valor)

# Caso seja feito outra variavel depois da lista criada pelo '*variavel', a nova variavel será
# Correspondente ao ultimo indice/valor da lista, 'ultimo_valor = José', se forem feitas
# Mais variaveis após o '*variavel', elas obterão o indice em ordem decrescente