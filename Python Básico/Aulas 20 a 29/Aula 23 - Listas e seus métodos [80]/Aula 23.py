"""
Listas em Python (Suportam vários valores de qualquer tipo, inclusive outra lista)
Tipo list - Mutável`

Conhecimentos reutilizáveis (str) - índices e fatiamento
Métodos úteis: 

append - Adiciona um item ao final
insert - Adiciona um item no indice escolhido
pop - Remove do final ou do indice escolhido (Pode salvar o valor em uma variavel)
del - apaga um indice
clear - limpa a lista
extend - estende a lista
+ - concatena listas

Create Read Update Delete (CRUD):
Criar, ler, alterar, apagar = lista[i]
"""

#        012345
#        -54321
string = "ABCDE"  # Len: 5 caracteres

#         0     1          2         3    4
#        -5    -4         -3        -2   -1
lista = [123, True, "Gabriel Belo", 1.2, []]  # Lista = list()

# print(bool(lista))  # False: lista vazia
# print(lista, type(lista))  # Type: list

# Indices e fatiamento
print(lista[2].upper(), type(lista[2]))  # GABRIEL BELO -> str

# Lista = Mutavel
lista[-3] = "Jonas"
print(lista[2], type(lista[2]))
print(lista)  # Modifica dentro da lista


# Adicionar ou remover valores: altera todos os indices da lista (EVITAR EM LISTAS MUITO GRANDE)
lista2 = [10, 20, 30, 40]
lista2[2] = 300

del lista2[2]  
print(lista2)

lista2.append(50)  
print(lista2)

ultimo_valor = lista.pop()  
print(lista2, ultimo_valor)

lista2.insert(0, 5)
print(lista2)

lista2.clear()
print(lista2)


# Extend e +
lista_a = [1, 2, 3]
lista_b = [4, 5, 6]

lista_c = lista_a + lista_b
lista_d = lista_a.extend(lista_b)  # Nao retorna nada, mexe diretamente na lista_a
print(lista_c, lista_d, lista_a)
