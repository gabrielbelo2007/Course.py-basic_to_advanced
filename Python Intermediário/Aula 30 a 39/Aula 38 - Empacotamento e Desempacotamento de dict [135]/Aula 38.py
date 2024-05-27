"""
Empacotamento e Desempacotamento (padrão)

a, b = 1, 2
a, b = b, a
print(a, b)
"""

# Empacotamento e Desempacotamento - nos dicionarios

"""
pessoa = {
    "nome": "Aline", 
    "sobrenome": "Souza",
}

(a1, a2), (b1, b2) = pessoa.items()
print(a1, a2)
print(b1, b2)

for chave, valor in pessoa.items():
    print(chave, valor)
"""

pessoa = {
    "nome": "Aline", 
    "sobrenome": "Souza",
}

dados_pessoa = {
    "altura": 1.65,
    "idade": 17,
}

pessoas_completa = {**pessoa, **dados_pessoa}  # Desempacotar dicionarios
# print(pessoas_completa)

""" 
*args -> recebe argumentos não nomeados
**kwargs -> "keyword arguments", recebe argumentos nomeados, como o conjunto chave-valor dos dicts
"""

def mostrar_argumentos_nomeados(*args, **kwargs):
    print("Argumentos não nomeados:", args)
    
    for chave, valor in kwargs.items():
        print("Argumentos nomeados:", chave, valor)
        
mostrar_argumentos_nomeados(1, 2, nome="Gabriel", sobrenome="Belo")
mostrar_argumentos_nomeados(**pessoas_completa)
