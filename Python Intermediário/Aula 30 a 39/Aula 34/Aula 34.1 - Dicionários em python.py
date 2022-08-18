clientes = {
    'cliente1': {
        'nome': 'Gabriel',
        'sobrenome': 'Belo',
    },
    'cliente2': {
        'nome': 'João',
        'sobrenome': 'Morais',
    },
    'cliente3': {
        'nome': 'Isabel',
        'sobrenome': 'Gonçalves',
    }
}

for clientes_k, clientes_v in clientes.items():
    print(f'Os clientes são: {clientes_k}')
    print()
    for dados_n, dados_s in clientes_v.items():
        print(f'\t{dados_n} = {dados_s}')  # \t serve de espaçamento
    print()

d1 = {1: 'a', 2: 'b', 3: 'c', 4: ['Gabriel', 'Belo']}

# Cria uma cópia rasa, pois ainda é possível alterar itens mutáveis
# que pertencem ao dict original, como listas. dict secundários e etc...

d1_copia = d1.copy()
d1_copia[1] = 'mudou'  # Não alterou d1
d1_copia[4][0] = 'João'  # Alterou d1

print(d1)
print(d1_copia)

# Caso voce queria uma cópia onde os dict sejam independentes, usa-se:

import copy

d1_copia2 = copy.deepcopy(d1)
d1_copia2[4][0] = 'Gabriela'
print(d1_copia2)

# É possível fazer o cast. de listas (exemplo) para dicionários:

lista = [
    ['c1', 1],
    ['c2', 2],
    ['c3', 3]
]

d2 = dict(lista)
print(d2)

# A função '.pop' e o '.update' também funciona no dicts

d2.pop('c1')
print(d2)

d2.update(d1)
print(d2)
