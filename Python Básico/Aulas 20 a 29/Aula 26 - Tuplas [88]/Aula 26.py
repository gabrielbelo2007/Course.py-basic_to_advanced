"""
Tipo Tupla - Lista Imutavel
"""

nomes_lista = ["Maria", "Helena", 'Luiz']
nomes_tupla = "Gabriel", "Bel"

nomes_lista[0] = "Pode"

nomes_lista = tuple(nomes_lista)
# nomes_lista[0] = "Nao pode, tuplas sao imutaveis"

print(nomes_lista, nomes_tupla, type(nomes_tupla))
