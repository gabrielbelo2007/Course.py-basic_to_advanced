""" 
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro
"""

pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
#   'sobrenome': "Só esse valor seria utilizado",
    'idade': 900,
    'estado': "PE"
}

print(pessoa.keys())  # Imprime apenas as chaves
print(pessoa.values())  # Imprime os valores
print(pessoa.items())  # Imprime as chaves e os valores separados

for chave, valor in pessoa.items():
    print(chave, valor)
    
pessoa.setdefault("altura", 1.70)  # Se a chave não existir, ele cria e atribui esse valor
print(pessoa['altura'])
local = pessoa.setdefault("estado", "RN")  # Se a chave existir ele apenas pega o valor sem alterar
print(local)

print(pessoa.get("nome1", "Essa chave não existe"))  # Procura uma chave e imprime um valor se ela não existir

nome = pessoa.pop("nome")  # Exclui essa chave do dict mas retorna o valor dessa chave
print(nome)

ultima_chave = pessoa.popitem()  # Exclui a ultima chave do dict e retorna o par chave-valor
print(ultima_chave)

# Mesma coisa:
""" 
pessoa.update({
    'nome': 'novo valor',
    idade': 30,
})

tupla = (('nome', 'novo valor'), ('idade', 30))
pessoa.update(tupla)  # Pode receber iteraveis que tenham 2 valores para serem atribuidos como chave-valor

lista = [['nome', 'novo valor'], ['idade', 30]]
pessoa.update(lista) -> {'nome': 'novo valor', idade': 30}
"""
pessoa.update(nome='novo valor', idade=30)  # Atualiza valores de chaves ja existentes no dict
print(pessoa["nome"], pessoa["idade"])
