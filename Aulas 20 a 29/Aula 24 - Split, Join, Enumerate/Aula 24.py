"""
Split, Join e Enumerate em Python

* Split - Dividir uma string em uma lista  # str
* Join - Juntar uma lista  # str
* Enumerate - Enumerar elementos da Lista  # Funciona em iteráveis
"""

"""
SPLIT:

string_1 = "O Brasil é o país do futebol, o Brasil é penta"
lista_1 = string_1.split('a')
lista_2 = string_1.split(' ')

# Nos parenteses se coloca a partir do que vai ser feito a divisão; com a letra "a"
# As letras "a" minusculas vão ser cortadas para serem o marco de divisão dos valores na lista


for valor in lista_1:
    print(f'A palavra {valor} apareceu {lista_1.count(valor)}x veze(s) na frase.')
# Count - serve para contar quantas vezes o mesmo valor aparece


palavra = ''
contagem = 0

for valor1 in lista_2:
    qtd_vezes = lista_2.count(valor1)

    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor1

print(f'A palavra que mais apareceu é {palavra} ({contagem}x).')

string_2 = 'O Brasil é o o o país do futebol, o brasil é penta'
lista_3 = string_2.split(',')

for valor2 in lista_3:
    print(valor2.strip().capitalize())

# Função strip - remove espaços do inicio e do fim da str
# Função capitalize - deixa maiúsculo a primeira letra da str, e deixa as outras maisculas como
# letras minusculas, no caso "Brasil" ira aparecer como "brasil"
"""

"""
JOIN:

string_3 = "O Brasil é penta."
lista_4 = string_3.split(' ')
string_4 = ','.join(lista_4)

# Se escreve uma string com determinado valor, depois adiciona a lista nos parentes
# O join vai juntar os elementos da lista em uma string, a partir da string determinada

print(string_3)
print(lista_4)
print(string_4)
"""

"""
ENUMERATE:

string_5 = "O Brasil é penta."
lista_5 = string_5.split(' ')

for indice, valor3 in enumerate(lista_5):
    print(indice, valor3, lista_5[indice])

# O enumerate mostra os valores de uma lista junto com o seu indice
# lista_5[indice] == a variavel indice do enumerate junto com a variavel valor3 do for

# Sem usar Enumerate:

lista_6 = [  # Pode ter varias listas dentro de outra
    [0, 'João'],
    [1, 'Pedro'],
    [2, 'Maria'],
]

for indice, nome in lista_6:
    print(indice, nome)

# Usando Enumerate:

lista_7 = ['João', 'Pedro', 'Maria']

for ind, nome1 in enumerate(lista_7):
    print(ind, nome1)
"""