""" 
Comprehension em dicts e sets - mesmas funções em outros tipos de dados (não tão usual)
"""

# Dict

produto_dict = {
    "nome": "Caneta Azul",
    "preco": 2.5,
    "categoria": "Escritório",
}

dc_produto = {
    # Mapeamento
    chave: valor.upper()
    if isinstance(valor, (int, float)) else valor
    for chave, valor in produto_dict.items()
    if chave != "categoria" # Filtro
}

produto_list = [
    ("a", "valor a"),
    ("b", "valor b"),
    ("c", "valor c"),
]

dc_lista = {
    chave: valor
    for chave, valor in produto_list
}

# print(dict(produto_list)) -> Mesma funcionalidade

# Sets

s1 = {2 ** i for i in range(10)}
print(s1)
