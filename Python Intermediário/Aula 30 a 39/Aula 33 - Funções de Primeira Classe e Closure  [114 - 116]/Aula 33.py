
"""
Higher Order Functions
Funções de primeira classe (Executar funções dentro de outras funções)
"""

def saudacao(msg, nome):  # Função que será executada em outra função
    return f'{msg}, {nome}!'


def executa(funcao, *args):  # Recebe uma função e os argumentos dessa função
    return funcao(*args)  # Executa e retorna o valor dessa função com seus argumentos


print(
    executa(saudacao, 'Bom dia', 'Luiz')
)


"""  
Closure ("fechamento") e funções que retornam outras funções
"""

# Essa execução é correta porém muito demorada e trabalhosa
"""
def criar_saudacao(saudacao, nome):
    return f"{saudacao}, {nome}!"

s1 = criar_saudacao("Bom dia", "Luiz")
s2 = criar_saudacao("Boa noite", "Luiz")
"""

# Para resolver: podemos criar uma função que retorna uma função sem executar, assim teremos uma função principal para todas as saudações

def criar_saudacao(saudacao):
    def saudar(nome):
        return f"{saudacao}, {nome}!"
    return saudar  # Sem por os parenteses, a função não é executada mas fica salva na memória


bom_dia = criar_saudacao("Bom dia")  # bom_dia é a função "saudar", pois ela foi retornada por "criar_saudacao" sem ser executada
print(bom_dia("Gabriel"))  # Assim podemos executar "bom_dia" (== saudar), atribuindo apenas o argumento "nome" da função "saudar"


# Dessa forma temos uma função principal retornando outra função não executada, assim guardando seus argumentos 
boa_noite = criar_saudacao("Boa noite")
print(boa_noite("Gabriel"))  # Onde depois podemos executar e usar esses argumentos guardados, essa execução é chamada de CLOSURE:
# O argumento atribuído a variável "boa_noite" é o "fechamento" necessário para que a função "saudar" seja executada e retire seus args da memória
