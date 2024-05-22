""" 
Dicionários são estruturas de dados do tipo: par de "chave" e "valor".
Chaves podem ser consideradas como o "índice" que vimos na lista e podem ser de tipos imutáveis -> str, int, float, bool, tuple...

O valor pode ser de qualquer tipo, incluindo outro dicionário.
Usamos as chaves - {} - ou a classe dict para criar dicionários.
Imutáveis: str, int, float, bool, tuple
Mutável: dict, list
"""
# pessoa = dict(nome='Luiz Otávio', sobrenome='Miranda') -> Uma forma de construir um dicionário

# Forma mais usual de construção de dicionários
pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
    'idade': 18,
    'altura': 1.8,
    'endereços': [
        {'rua': 'tal tal', 'número': 123},
        {'rua': 'outra rua', 'número': 321},
    ]
}

print(pessoa["nome"])  # Os índices são as chaves que acessam os valores atribuídos no dict
print(pessoa["sobrenome"])

for chave in pessoa:
    print(chave, ":", pessoa[chave])


""" 
Manipulando chaves e valores em dicionários
"""

# Adicionar elementos no dict
dicionario = {}
dicionario['valor'] = 10
print(dicionario)

# Altera a chave de maneira mais eficiente
chave_dinamica = 'novo_valor'
dicionario[chave_dinamica] = '20'
print(dicionario[chave_dinamica])


del dicionario["valor"]  # Apaga um par de chave-valor
print(dicionario)

if dicionario.get('sobrenome') is None:  # Por padrão o ".get" retorna "None" caso a chave procurada não exista
    print('Essa chave não existe!')  # Procurar uma chave sem o ".get" retorna um ERRO
else:
    print(dicionario['sobrenome'])
