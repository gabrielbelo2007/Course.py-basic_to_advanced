""" 
split e join com Lista e str

split - divide uma string
join - une uma string
strip - retira caracteres de uma string do inicio e do final
"""

frase = "     Olha que,     coisa interessante"
lista_frases_separadas = frase.split(",")  # Divide os valores da str divididos pela "," e armazena em uma lista

lista_frases_juntas = []
for i, frase in enumerate(lista_frases_separadas):
    lista_frases_juntas.append(lista_frases_separadas[i].strip())  # Remove os espacos em branco  
    
print(lista_frases_separadas)
print(lista_frases_juntas)

frases_unidas = '-'.join(lista_frases_juntas) # Une iteraveis e define um separador
print(frases_unidas)
