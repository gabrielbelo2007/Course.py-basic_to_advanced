perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 2 + 2',
        'respostas': {
            'a': '1',
            'b': '4',
            'c': '5',
        },
        'resposta_certa': 'b',
    },
    'Pergunta 2': {
        'pergunta': 'Quanto é 3 x 2',
        'respostas': {
            'a': '4',
            'b': '5',
            'c': '6',
        },
        'resposta_certa': 'c',
    },
}

respostas_certas = 0
for chave_p, chave_r in perguntas.items():
    print(f'{chave_p}: {chave_r["pergunta"]}')

    print()
    print('Escolha as opções abaixo: ')
    for rk, rv in chave_r['respostas'].items():
        print(f'[{rk}]: {rv}')

    resposta_usuario = input('Sua resposta: ')
    print()

    if resposta_usuario == chave_r['resposta_certa']:
        print('Você acertou!')
        respostas_certas += 1
    else:
        print('Você errou!')

    print()

qtd_perguntas = len(perguntas)
porcentagem_acerto = respostas_certas / qtd_perguntas * 100

print(f' Você acertou {respostas_certas} perguntas.')
print(f' Sua porcentagem de acerto foi de {porcentagem_acerto}%.')
