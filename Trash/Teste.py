

nome_1 = 'Gabriel'
sobrenome = 'Belo'
nome_formatado = '{0} {1:#^50}'.format(nome_1, sobrenome)
print(f'{nome_1:#^50}')
print(nome_formatado)

num_4 = 1
print(f'{num_4:0>10}')  # a variavel tem que ter 10 casas contando com o número principal
