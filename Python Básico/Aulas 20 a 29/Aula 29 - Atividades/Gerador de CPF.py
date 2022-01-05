from random import randint
cpf = str(randint(100000000, 999999999))

novo_cpf = cpf

contador = 8
numerador = 10
valor_temp = 0
total = 0
validar = 0

for valor in novo_cpf:
    valor = int(valor)
    while contador < 9:
        valor_temp = valor * numerador
        contador += 1
        numerador -= 1
    contador = 8
    total += valor_temp

validar = 11 - (total % 11)
if validar > 9:
    validar = 0
    novo_cpf += str(validar)

else:
    novo_cpf += str(validar)

total = 0
numerador = 11
valor_temp = 0

for valor in novo_cpf:
    valor = int(valor)
    while contador < 9:
        valor_temp = valor * numerador
        contador += 1
        numerador -= 1
    contador = 8
    total += valor_temp

validar = 11 - (total % 11)
if validar > 9:
    validar = 0
    novo_cpf += str(validar)

else:
    novo_cpf += str(validar)

print(novo_cpf)