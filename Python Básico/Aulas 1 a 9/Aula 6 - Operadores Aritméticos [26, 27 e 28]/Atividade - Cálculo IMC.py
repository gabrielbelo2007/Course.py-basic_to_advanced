# Calculando o IMC

nome = input("Qual o seu nome? ")
altura = input("Qual sua altura? ")
peso = input("Qual seu peso? ")

altura = altura.replace(",", ".")
alt = float(altura)
IMC = int(peso) / (alt ** alt)

print(f"{nome}, tem {altura}m de altura, pesa {peso}kg e seu IMC é {IMC:.2f}")
