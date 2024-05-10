# continue -> pula uma etapa do while

"""
contador = 0

while contador <= 100:
    contador += 1

    if contador == 6:
        print("Sem mostrar o 6")
        continue  # Retorna para o inicio do while

    if contador >= 10 and contador <= 27:
        print("Sem mostrar o", contador)
        continue

    print(contador)

    if contador == 40:
        break
  
print("Acabou!")
"""

# Whiles internos

"""
qtd_linhas = 5
qtd_colunas = 5

linha = 1
while linha <= qtd_linhas:
    
    coluna = 1
    while coluna <= qtd_colunas:  # A cada linha gera 5 colunas
        print(f"{linha=}, {coluna=}")  # O "=" mostra o nome da variavel antes do valor
        coluna += 1
        
    linha += 1    

print("Acabou!")
"""

# While + Else (Executado quando o while se torna FALSE)

string = "Valor qualquer"

i = 0

while i < len(string):
    letra = string[i]
    
    if letra == " ":
        break
    
    print(letra)
    i += 1
    
else:
    print("O else dentro do while foi executado")

print("Fora do while")