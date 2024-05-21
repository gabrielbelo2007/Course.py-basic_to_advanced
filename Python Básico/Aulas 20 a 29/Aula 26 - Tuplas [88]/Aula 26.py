"""
Tipo Tupla - Lista Imutavel

Diferentemente da lista não é possível modificar valores na tuple
De resto é basicamente o mesmo princípio, e também pode ser convertida em lista
"""

nomes_lista = ["Maria", "Helena", 'Luiz']
nomes_tupla = "Gabriel", "Bel"

nomes_lista[0] = "Pode"

nomes_lista = tuple(nomes_lista)
# nomes_lista[0] = "Nao pode, tuplas sao imutaveis"

print(nomes_lista, nomes_tupla, type(nomes_tupla))
