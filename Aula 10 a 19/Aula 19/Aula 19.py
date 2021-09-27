"""
While / Else
Contadores
Acumuladores
"""

contador = 1
acumulador = 1

while contador <= 10:
    print(contador, acumulador)

    if contador > 5:
        break

    acumulador = acumulador + contador
    contador += 1

else:  # o else só sera executado quando 'while' for False, indepentedente do 'break'
    print('Cheguei no else.')
print('Isso será executado')
