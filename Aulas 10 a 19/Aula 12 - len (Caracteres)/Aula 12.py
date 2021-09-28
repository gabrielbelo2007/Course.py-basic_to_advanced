"""
len - Contador de caracteres (não funciona com numeros)
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
# No segundo caso os numeros não são somados, tomar cuidado com fechar as chaves
