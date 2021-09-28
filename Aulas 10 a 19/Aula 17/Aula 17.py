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
print(texto[:-2])  # retira oq está no índice e tudo q vem dps dele

nova_string = texto[2:6]  # fatiamento de str
nova_string1 = texto[:6]  # sem número no 'inicio' ele começa do 0
nova_string2 = texto[5:]  # sem número no 'fim' ele vai até o ultimo indice
nova_string3 = texto[::2]  # o passo de leitura

print(nova_string)
print(nova_string1)
print(nova_string2)
print(nova_string3)

for letra in texto:
    print(letra)
