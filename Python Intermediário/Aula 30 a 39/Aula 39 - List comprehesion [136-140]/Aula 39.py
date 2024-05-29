"""
List comprehension é uma forma rápida para criar lista a partir de iteráveis
-> Usado para otimizar e encurtar códigos
""" 

# Criando uma lista com 10 valores
# print(list(range(10)))


# Método de adicionar cada número até atingir 10 valores
lista = []
for numero in range(10):
    lista.append(numero)
# print(lista)


# Laços e Condicionais dentro de uma lista
lista_nova = [numero for numero in range(10)]  # Primeiro põe o que será adicionado na lista, e depois a condição ou o laço
# print(lista)


# Mapeamento de dados em list comprehension - Direita do laço "FOR" 
# -> Gera uma nova lista de mesmo tamanho da inicial (caso não haja filtro) com os valores de mesmo índice alterados)

produtos = [
    {"nome": "p1", "preco": 20, },
    {"nome": "p2", "preco": 10, },
    {"nome": "p3", "preco": 30, },
]

novos_produtos = [
    # Mapeamento
    {**produto, "preco": produto["preco"] * 1.05} # Aumentando em 5% os precos em comparação a lista "produtos"
    if produto["preco"] > 20 else {**produto}  # Operação ternária dentro do comprehension: "valor" if "condicao" else "valor_alternativo"
    for produto in produtos
    if produto["preco"] > 10  # Filtro (Condicional simples)
]

print(*novos_produtos, sep="\n")


# Filtrar uma lista - Direita do "FOR"

lista_filtrada = [n for n in range(10) if n < 5 ]  
print(lista_filtrada)

 
# Mais de um "FOR" por list comprehension

exemplo_comum = []
for x in range(3):
    for y in range(3):
        exemplo_comum.append((x, y))
print(exemplo_comum)

dois_lacos_for = [
    (x, y)  # Os parênteses apenas colocam os valores em tuplas
    for x in range(3)
    for y in range(3)
]
print(dois_lacos_for)
