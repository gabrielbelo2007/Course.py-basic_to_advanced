
cpf = [0, 2, 2, 7, 0, 7, 7, 9, 4, 6, 0]
novo_cpf = cpf[:-2]

contador = 8
numerador = 10
valor_temp = 0
total = 0

for valor in novo_cpf:
    while contador < 9:
        valor_temp = valor * numerador
        contador += 1
        numerador -= 1
    contador = 8
    total += valor_temp

else:
    validar = 11 - (total % 11)
    if validar > 9:
        validar = 0
        novo_cpf.append(validar)

    else:
        validar = validar
        novo_cpf.append(validar)

total = 0
numerador = 11
valor_temp = 0

for valor in novo_cpf:
    while contador < 9:
        valor_temp = valor * numerador
        contador += 1
        numerador -= 1
    contador = 8
    total += valor_temp


else:
    validar = 11 - (total % 11)
    if validar > 9:
        validar = 0
        novo_cpf.append(validar)

    else:
        validar = validar
        novo_cpf.append(validar)

if novo_cpf == cpf:
    print('O seu CPF é valido!')
    print(novo_cpf)
else:
    print('O seu CPF é invalido!')
    print(novo_cpf)