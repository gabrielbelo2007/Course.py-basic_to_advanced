"""
Manipulando Strings

String indices
Fatiamento de Strings [inicio:fim:passo]
Funções built-in len, abs, type, print...
-Essas funções podem ser usadas diretamente em cada tipo.
"""

# positivos   [012345678]
texto =       'Python s2'
# negativos  -[987654321]

print(texto[2])
print(texto[:-2])  # Retira o o índice e tudo que vem após ele

nova_string = texto[2:6]  # O número que determina a parada do fatiamento não conta
nova_string1 = texto[:6]  # Sem número no 'inicio' ele começa do 0
nova_string2 = texto[5:]  # Sem número no 'fim' ele vai até o último indice
nova_string3 = texto[::2]  # O passo de leitura
nova_string4 = texto[::-1]  # Negativo além de alterar o passo inverte a ordem de leitura

print(nova_string)
print(nova_string1)
print(nova_string2)
print(nova_string3)
print(nova_string4)

for letra in texto:
    print(letra)
