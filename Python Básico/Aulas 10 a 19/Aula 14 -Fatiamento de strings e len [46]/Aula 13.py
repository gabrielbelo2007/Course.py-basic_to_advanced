"""
Fatiamento de Strings [inicio:fim:passo]
# positivos   [012345678]

# negativos  -[987654321]
len - Retorna a qtd de caracteres da str (não funciona com números)
"""

senha = input('Digite seu usuario: ')
qtd_caracteres = len(senha)  # considera espaços

print(senha, qtd_caracteres, type(qtd_caracteres))

if qtd_caracteres < 6:
    print('Você precisa digitar pelo menos 6 caracteres')
else:
    print('Você foi cadastrado no sistema.')

string_1 = input('Digite alguma coisa: ')
string_2 = input('Digite outra coisa: ')

print(f"A quantidade total de caracteres digitados foi {len(string_1) + len(string_2)}")
print()
print(f"A quantidade total de caracteres digitados foi {len(string_1)} + {len(string_2)}")
# No segundo caso os números não são somados, tomar cuidado com fechar as chaves

texto1 = "teste"

print(texto1[:-2])  # Retira o o índice e tudo que vem após ele

nova_string = texto1[2:6]  # O número que determina a parada do fatiamento não conta
nova_string1 = texto1[:6]  # Sem número no 'inicio' ele começa do 0
nova_string2 = texto1[5:]  # Sem número no 'fim' ele vai até o último indice
nova_string3 = texto1[::2]  # O passo de leitura
nova_string4 = texto1[::-1]  # Negativo além de alterar o passo inverte a ordem de leitura
