def executa(funcao, *args):
    return funcao(*args)

"""
def soma(x, y):
    return x + y
"""

print(
    executa(lambda x, y: x + y, 2, 3)  # = def soma
)

"""
def cria_multiplicador(multiplicador):
    def multiplica(numero):
        return numero * multiplicador
    return multiplica
    
duplica = cria_multiplicador(2)
"""

triplica = executa(  
    lambda m: lambda n: n * m, 3  # = def cria_multiplicador, funcoes com funcoes internas nao costumam usar lambda
)  # O argumento "3" -> m da lambda

print(triplica(2))  # O argumento "2" -> n da lambda
