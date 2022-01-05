
cpf = input('Qual é o seu CPF: ')
novo_cpf = cpf[:-2]

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

sequencia = novo_cpf == str(novo_cpf[0]) * len(cpf)

if novo_cpf == cpf and not sequencia:
    print('O seu CPF é valido!')
    print(novo_cpf)
else:
    print('O seu CPF é invalido!')
    print(novo_cpf)