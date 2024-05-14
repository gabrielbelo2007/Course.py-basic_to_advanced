"""
    Cuidados com dados mutaveis
    = : copiado o valor (imutaveis)
    = : aponta para o mesmo valor na memoria (mutavel)
"""

# Dados imutaveis apenas se copiam
str_a = "Joao"
str_b = str_a

str_a = "Maria"
print(str_a, str_b)  # a str_b apenas copiou o valor inicial da str_a


# Dados mutaveis apontam para o mesmo valor
lista_a = [1, 2, 3]
lista_b = lista_a

print(lista_a, lista_b)

lista_a[0] = 2
print(lista_a, lista_b)  # lista_b aponta para o mesmo valor de lista_a, nao tem copia

# Para copiar dados mutaveis
lista_c = lista_a.copy()

lista_a[1] = 3
print(lista_a, lista_b, lista_c)
