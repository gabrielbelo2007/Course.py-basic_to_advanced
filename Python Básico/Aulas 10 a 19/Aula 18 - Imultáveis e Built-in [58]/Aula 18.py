# Imutavéis: str, int, float, bool

string = "Gabriel Belo"
# string[3] = "ABC" (Isso nao pode ser feito pois str = imutavel)

# Exemplo de como pode ser feito:
outra_variavel = "ABC"
print(f"{string[:3]}{outra_variavel}{string[4:]}")
