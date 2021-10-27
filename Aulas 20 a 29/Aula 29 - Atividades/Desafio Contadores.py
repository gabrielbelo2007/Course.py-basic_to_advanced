"""
contador = [10]
final = 0
diminuir = 9

for pr, re in enumerate(contador):
    print(pr, re)
    contador.append(diminuir)
    diminuir -= 1
    if diminuir == final:
        break
"""

'''
contador = 0
numerador = 10

while contador < 9:
    print(contador, numerador)
    contador += 1
    numerador -= 1
'''

'''
Maneira usada pelo professor:

for p, r in enumerate(range(10, 1, -1)):
    print(p, r)
'''