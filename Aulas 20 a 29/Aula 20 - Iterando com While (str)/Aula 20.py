#        Indices
#        0123456789.......................33

frase = 'O rato roeu a roupa do rei de roma'  # Valor iteravel
tamanho_frase = len(frase)
nova_string = ''
contador = 0

letra_maiscula = input('Qual letra deseja colocar maiscula: ')

# Iteração / Iterar (ato de percorrer cada elemento da sua str, ou do elemento iteravel)

while contador < tamanho_frase:
    # print(frase[contador], contador)
    letra = frase[contador]

    if letra == letra_maiscula:
        nova_string += letra_maiscula.upper()

    else:
        nova_string += frase[contador]
    contador += 1

print(nova_string)
print(frase)