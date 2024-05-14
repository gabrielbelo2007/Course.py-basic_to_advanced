"""
enumerate - enumera iteraveis (indices)
"""

lista = ["Maria", "Helena", "Luiz"]
lista.append("Joao")

lista_enumerada = enumerate(lista)
# print(lista_enumerada)  # Retorna um iterador e nao os valores da lista numerados
print(list(lista_enumerada))

for item in lista_enumerada:  
    print(item)

print(lista_enumerada)  # Quando o enumerate esta em uma variavel, depois do FOR ele fica "sem valores"


for indice, nome in enumerate(lista):  # Desempacota dentro do proprio FOR
#   indice, nome = item  (caso no lugar de indice, nome fosse item)
    print(indice, nome)
