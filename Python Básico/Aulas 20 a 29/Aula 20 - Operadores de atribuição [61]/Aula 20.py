"""
Operadores de atribuicao

= ; += ; -= ; *= ; /= ; //= ; **= ; %=

"""
contador = 0

contador += 3  # contador = contador + 1 [Soma]
print(contador)

contador -= 1  # contador = contador - 1 [Subtracao]
print(contador)

contador *= 2  # contador = contador * 2 [Multiplicacao]
print(contador)

contador /= 2  # contador = contador / 2 [Divisao - float]
print(contador)

contador //= 2  # contador = contador // 2 [Divisao - int]
print(contador)

contador **= 2  # contador = contador ** 2 [Potenciacao]
print(contador)

contador %= 2  # contador = contador % 2 [Resto de divisao]
print(contador)