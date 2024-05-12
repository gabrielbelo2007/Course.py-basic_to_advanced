"""
while - Loop utilizado quando nao se sabe quantas repeticoes vao ser realizadas

for - Loop utilizado para repeticoes determinadas e finitas (break, else, continue, etc)

Range -> range(start, stop, step)
"""

# For:


texto = "Python"
"""
novo_texto = ""

for letra in texto:  # Itera sobre o elemento guardando uma iteracao por vez em uma variavel
    print(letra)
    novo_texto += f"*{letra}"

print(novo_texto + "*")
"""

# For + Range:

for n, letra in enumerate(texto):  # enumerate mostra o indice das letras do texto
    print(n, letra)

for n in range(3, 10, 2):  # O número do stop não aparece na leitura
    print(n)

for n1 in range(10):  # o 'stop' e 'step' nesse caso estão omitidos ficando PADRÃO
    print(n1)

for n2 in range(20, 10, -1):  # 20 = 'start', -1 = 'step' (como sera feito a contagem)
    print(n2)
    
numeros_pares = range(0, 100, 8)  # Pode ser usado para saber os multiplos existente entre dois numeros
print(numeros_pares)