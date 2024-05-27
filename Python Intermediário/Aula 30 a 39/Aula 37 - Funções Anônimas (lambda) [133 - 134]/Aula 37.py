# Introdução à função lambda (função anônima de uma linha)
# A função lambda é uma função como qualquer outra em Python. 
# Porém, são funções anônimas que contém apenas uma linha, ou seja, tudo deve ser contido dentro de uma única expressão.

"""
lista = [4, 32, 1, 34, 5, 6, 6, 21, ]
lista.sort(reverse=True)  # Ordena valores como numeros e letras, em ordem crescente ou decrescente
sorted(lista)  # Ordena e cria uma copia rasa da lista
"""

# Para ordernar valores não ordenaveis naturalmente
lista1 = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]

"""
def ordena(item):
    return item["nome"]  # Ordenando pelos nomes (Python usa tabela unicode para saber a ordem das letras)

lista1.sort(key=ordena)  # "key=" passa uma função que o ".sort" vai utilizar para ordernar a lista
"""

def exibir(lista):
    for linha in lista:
        print(linha)
    print()

lista_nomes =  sorted(lista1, key=lambda item: item["nome"])  # A "def ordena" feita em uma unica linha, anonima pois nao pode ser chamada em outro local
lista_sobrenomes = sorted(lista1, key=lambda item: item["sobrenome"])

exibir(lista1)
exibir(lista_nomes)
exibir(lista_sobrenomes)
