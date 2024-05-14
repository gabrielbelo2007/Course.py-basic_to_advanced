"""
Desempacotamento de Listas
"""

lista_1 = ['João', 'Maria', 'Pedro']
n1, n2, n3 = lista_1

print(n1)
# As variaveis 'n' foram ligadas aos indices do valores da lista, ou seja
# n1 = Indice 0 = João    e assim por diante


# Quando usar o desempacotamento é necessario criar uma variavel para cada indice
# Caso não seja necessario para o seu objetivo todos os valores da lista
# Após desempacotar os necessários cria uma variavel com * na frente que guarda os valores restantes
# Geralmente usa-se "_" para o nome da variavel se os valor(es) nao forem ser usados

lista_2 = ['Leo', 'Guigas', 'Mendes', 'Luiz', 'Ruan', 'Ian']
n4, n5, *resto_valor, penultimo_valor, ultimo_valor = lista_2

print(n4, n5, resto_valor, penultimo_valor, ultimo_valor)

# Caso seja feito outra variavel depois da lista criada pelo '*resto_valor', a nova variavel será
# Correspondente ao ultimo indice/valor da lista, 'ultimo_valor = Ian', se forem feitas
# Mais variaveis após o '*variavel', elas obterão o indice em ordem decrescente


lista_3 = [1, 2, 3]
num_1, num_2, num_3, *_ = lista_3

print(*_)

# A variavel "guarda-valores" esta vazia, porem se mais valores forem adicionados a lista, ela vai armazena-los