# Usado para otimizar e encurtar códigos

l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
ex1 = [variavel for variavel in l1]  # Iterou uma lista anterior para criar uma
print(ex1)

ex2 = [v * 2 for v in l1]  # Multiplicou cada valor de l1 por 2 criando uma lista
print(ex2)

ex3 = [(v, v2) for v in l1 for v2 in range(3)]  # Formando "coordenadas"
print(ex3)

l2 = ["Gabriel", "Cunha", "Maria"]
ex4 = [v.replace("a", "@") for v in l2]  # Alterou os valores de A por @
print(ex4)

tupla = (
    ('chave', 'valor'),
    ('chave2', 'valor2'),
)

ex5 = [(y, x) for x, y in tupla]  # Transformou a tupla em lista e inverteu os valores
print(ex5)

############################################################################

l3 = list(range(100))

ex6 = [v for v in l3 if v % 3 == 0 and v % 8 == 0]  # Filtrando a lista por números divisiveis por 3 e 8
print(ex6)

ex7 = [v if v % 3 == 0 else 0 for v in l3]  # Quando não for divisivel por 3 irá aparecer 0
print(ex7)

