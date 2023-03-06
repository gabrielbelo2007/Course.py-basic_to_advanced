"""
Condições IF, ELIF e ELSE
"""

if True:
    print('Verdadeiro.')  # os 4 espaços servem pare representar a hieraquia

    num_1 = 2
    num_2 = 4

    print(num_1 + num_2)

if True:
    print('Verdadeiro.')
else:  # Não pode ser executada sozinha
    print('Não é verdadeiro')

print('A minha expressão verdadeira')  # Não faz parte da hieraquia

if False:
    print('Verdadeiro.')

elif True:
    print('Agora é verdadeiro.')
    nome = input('Qual é o seu nome? ')

    print(f'O seu nome é {nome}')

elif True:  # Não vai ser lido pois já tem um "elif true" antes
    print('Mais uma Verdadeira')
    print(22 + 22)

else:  # É executado quando nenhuma das expressões anteriores forem 'True'
    print('Não é Veradeiro.')
