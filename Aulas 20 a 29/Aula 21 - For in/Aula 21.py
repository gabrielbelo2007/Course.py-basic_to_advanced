"""
'For in' em Python
Iterando strings com for
Função range: start=0, stop(sempre termina um número antes), step=1 - PADRÃO
"""

# continue - Pula para o proximo laço
# break - termina o laço

texto = 'Python'
nova_string = ''

for letra in texto:
    if letra == 't':
        nova_string += letra.upper()
    elif letra == 'h':
        nova_string += letra.upper()
    else:
        nova_string += letra

print(nova_string)


for n, letra in enumerate(texto):  # enumerate mostra o indice das letras do texto
    print(n, letra)

for n in range(3, 10, 2):  # O número do stop não aparece na leitura
    print(n)

for n1 in range(10):  # o 'stop' e 'step' nesse caso estão omitidos ficando PADRÃO
    print(n1)

for n2 in range(20, 10, -1):  # 20 = 'start', -1 = 'step' (como sera feito a contagem)
    print(n2)

for n3 in range(100):
    if n3 % 8 == 0:
        print(n3)

print('##########')

for n4 in range(0, 100, 8):  # mesma coisa do comando acima
    print(n4)
