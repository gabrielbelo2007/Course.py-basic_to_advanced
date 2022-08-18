# Funciona como uma lista, porém não tem indices criados automaticamente
# Voce organiza os indices nas funções e esses indices são chamados chaves
# Um dicionário é uma estrutura de dados que suporta pares de chaves e valores

d1 = {'chave1': 'valor da chave'}
d1['nova_chave'] = 'valor da nova chave'

print(d1)

# Outra forma de criar um dicionário

d2 = dict(chave2='Valor da chave', chave3='Valor da outra chave')
print(d2['chave2'])

# Caso exista mais de uma chave em um dicionário com o mesmo nome, apenas o
# último valor atribuída a ela vai aparecer, isso ocorre porque cada chave
# deve ter um valor unico

d3 = {'chave4': 'valor da chave', 'chave4': 'valor real da chave'}
print(d3['chave4'])

# Para nomear chaves, pode-se utilizar apenas valores imutáveis

d4 = {
    'str': 'valor',
    123: 'Outro valor',
    (1, 2, 3, 4): 'Tupla',
}

# IMPORTANTE saber que caso voce utilize uma chave que não está no dict
# será apresentado o erro e nada após será executado

d5 = {'teste': 'demo', 'chave1': 'valor1'}

if 'naoexiste' in d5:
    print(d5['naoexiste'])

# ou

if d5.get('naoexiste'):
    print(d5['naoexiste'])

# Para alterar o valor de chaves já existentes no dict

d5['teste'] = 'novo valor'
d5.update({'teste': 'novo valor'})
print(d5)

# Quando checamos um dict o foco é as chaves, para checar os valores,
# usamos a função '.values', para acessar tanto na função 'in' e no
# laço for

for k in d5.values():
    print(k)

# Caso queira tanto a chave como o valor, usa-se o '.items()'

for k in d5.items():
    print(k)

# A função len conta a quantidade de pares 'chave: valor' em um dict
