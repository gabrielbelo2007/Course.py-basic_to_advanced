"""
N = 2
etapa_1 = 50, 450, 10
etapa_2 = 30, 1000, 20
T_1 = etapa_1[0]
T_2 = etapa_2[0]
S_1 = etapa_1[1]
S_2 = etapa_2[1]
V_1 = etapa_1[2]
V_2 = etapa_2[2]

resultado_1 = S_1 / V_1
resultado_2 = S_2 / V_2

if resultado_1 >= T_1:
    print('NAO')
else:
    print('SIM')

if resultado_2 >= T_2:
    print('NAO')
else:
    print('SIM')
"""

N = int(input('Quantidade de Etapa(s): '))

total_1 = ''
temp = ''

while N > 0:
    etapa = input('Informações da Etapa: ')
    temp = etapa
    N -= 1
    if temp == etapa:
        temp += ' '
    total_1 += temp

etapa_1 = total_1.split(' ')
etapa_1.pop()
print(len(etapa_1))

T_1 = int(etapa_1[0])
T_2 = int(etapa_1[3])
S_1 = int(etapa_1[1])
S_2 = int(etapa_1[4])
V_1 = int(etapa_1[2])
V_2 = int(etapa_1[5])

resultado_1 = S_1 / V_1
resultado_2 = S_2 / V_2

if resultado_1 >= T_1:
    print('NAO')
else:
    print('SIM')

if resultado_2 >= T_2:
    print('NAO')
else:
    print('SIM')


