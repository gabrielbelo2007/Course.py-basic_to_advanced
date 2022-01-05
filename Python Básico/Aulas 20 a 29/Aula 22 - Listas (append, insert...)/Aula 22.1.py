# Continuação

secreto = 'perfume'
digitadas = []
chances = 3

while True:
    if chances <= 0:
        print('Você perdeu!')
        break

    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Isso não vale, digite apenas uma letra.')
        continue

    digitadas.append(letra)

    if letra in secreto:
        print(f'Parabens "{letra}" existe na palavra secreta.')

    else:
        print(f'Que pena,"{letra}" NÃO EXISTE na palavra secreta.')
        digitadas.pop()

    secreto_temporario = ''

    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

    if chances >= 0:
        tent_palavra = input('Gostaria de tentar a palavra : ')
        if tent_palavra == secreto:
            print(f'Que legal, você ganhou! A palavra era "{tent_palavra}".')
            break
        elif tent_palavra == 'n':
            print(f'Você tem {chances} chance(s).')
            print()
        else:
            chances = 0

    if secreto_temporario == secreto:
        print(f'Que legal, você ganhou! A palavra era "{secreto_temporario}".')
        break

    else:
        print(f'A palavra secreta está assim: {secreto_temporario}.')

    if letra not in secreto:
        chances -= 1

