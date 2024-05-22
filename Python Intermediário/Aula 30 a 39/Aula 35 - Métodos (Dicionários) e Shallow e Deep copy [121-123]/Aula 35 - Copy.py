d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0, 1, 2],
}
# d2 = d1  # d2 -> Não é um novo dict apenas aponta para o mesmo, as alterações mudam ambos
d2 = d1.copy()  # Cria uma "cópia rasa", pois ainda é possível alterar itens mutáveis, os imutaveis criam um novo dict

d2['c1'] = 1000  # Não alterou d1
d2['l1'][1] = 999999  # Alterou d1

print(f"Esse é o d1: {d1}")
print(f"Esse é o d2: {d2}")


print()
# Caso voce queria uma cópia onde os dict sejam independentes, usa-se:
import copy  # Biblioteca.py para fazer o "deepcopy"

d2 = copy.deepcopy(d1)

d2["l1"][0] = 'Gabriela' # Alterou apenas d2 mesmo sendo mudando um item mutável
print(f"Esse é o d1: {d1}")
print(f"Esse é o d2: {d2} cópia profunda")
