"""
Repeticões / Contadores
While (Enquanto): Executa uma ação enquanto uma condição for verdadeira
"""

"""
# Loop infinito -> Quando um codigo n tem fim
CONDICAO = True

while condicao:
    nome = input("Qual seu nome: ")
    print(f"Seu nome: {nome}")

# print(123) # Nunca vai ser executada pois esse while nao esta sendo quebrado
    break

print(123) # vai ser executado
"""

contador = 0

while contador <= 10:
    print(contador)
    contador += 1

contador -= 1
print(f"Contador contou ate: {contador}, acabou!")
