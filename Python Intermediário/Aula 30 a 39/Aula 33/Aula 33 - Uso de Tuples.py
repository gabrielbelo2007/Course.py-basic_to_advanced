# Diferentemente da lista não é possível modificar valores na tuple
# De resto é basicamente o mesmo princípio, e também pode ser convertida em lista

# Isto é uma tupla (com nenhum valor)
t1 = ()
print(type(t1))

# Isto também é uma tupla

t2 = 1, 2, 3, 4, 5
print(type(t2))

# Uma tupla sem paretenses com apenas um valor

t3 = 6, 7, 8, 9, 10, 11
print(type(t3))

# É possível acessar indices e interar os valores, concatenar e desempacotar

t4 = (1, 2, 3, "a", "Gabriel")
print(t4[1])

for v in t4:
    print(v)

t5 = t2 + t3

n1, n2, n3, *_, n11 = t5
print(n11)

# Também pode-se utilizar multiplicadores de repetição em tuplas

t6 = ('oi', 'tudo bem') * 3
print(t6)

# Conversão para lista (alterar algum valor da tupla)

t7 = (1, 2, 3, 4, 5)
print(t7)

t7 = list(t7)
t7[1] = 'mudei'
t7 = tuple(t7)
print(t7)


