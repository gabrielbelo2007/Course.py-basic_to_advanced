n = '49857428'

mult = 2
numerador = 1
total = 0
valor_temp = 0

for valor in n:
    valor = int(valor)
    while numerador < 2:
        valor_temp = valor * mult
        numerador += 1
        if valor_temp >= 10:
            valor_temp = str(valor_temp)
            v1, v2 = valor_temp
            valor_temp = int(v1) + int(v2)
        if mult == 2:
            mult -= 1
        else:
            mult += 1
    numerador = 1
    total += valor_temp

total_1 = total % 10
if total_1 == 0:
    s = 'SIM'
    print(s)
else:
    s = 'NÃO'
    print(s)
