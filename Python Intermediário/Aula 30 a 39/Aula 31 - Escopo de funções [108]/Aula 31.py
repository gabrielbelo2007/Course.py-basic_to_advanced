""" 
Escopo significa o local onde aquele código é executado.
Existe o escopo global e local, escopo é acessado de dentro para fora, nunca o contrário.

O escopo global é o escopo onde todo o código consegue executar.
O escopo local é o escopo onde apenas nomes do mesmo local podem executar.

Não temos acesso a nomes de escopos internos nos escopos externos.
A palavra "global" faz a variável do escopo local ser = a do escopo global.
"""

x = 1  # Pode ser executado por todo o código

def escopo_global():\
#   global x -> consegue manipular o "x" do escopo global
    x = 10
    
    def escopo_local():
        y = 2  # Só pode ser executado dentro do local dessa func: escopo_local
        print(x, y)  # Usa o "x" (10) do escopo local da func: escopo_global
    escopo_local()  # Essa func só pode ser executada dentro do local da func: escopo_global
    
# escopo_local() -> Função não existe no escopo global e não pode ser executada


print(x) # Usa o "x" do escopo global
escopo_global()  # Usa o "x" do seu proprio escopo
print(x) # Não pode ser alterado pelo escopo local da função
