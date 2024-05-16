""" 
Desempacotamento em chamadas de métodos e funções
"""

string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'Python', 'é', 'legal'

# Desempacotamento padrão
# p, b, *_, ap, u = lista
# print(p, u, ap)


# Desempacotamento de função, ambos mostram a mesma coisa
print('Maria', 'Helena', 1, 2, 3, 'Eduarda') 
print(*lista)

# É possível utilizar em qualquer iteravel
print(*string)
print(*tupla)


""" 
Operação ternária (condicional de uma linha)
<valor> if <condicao> else <outro valor>
"""

condicao = 10 == 11  # False
variavel = 'Valor' if condicao else 'Outro valor'  # Condicao = False -> executa o Else
print(variavel)  # Outro valor

# Pode por para definir valores de uma variavel
digito = 9  # > 9 = 0
novo_digito = digito if digito <= 9 else 0  # Digito = 9 (True) -> novo_digito = digito
print(novo_digito)

novo_digito = 0 if digito > 9 else digito  # Digito > 9 (False) -> novo_digito = digito
print(novo_digito)

# Pode ter mais de um if/else
print('Valor' if False else 'Outro valor' if False else 'Fim')
