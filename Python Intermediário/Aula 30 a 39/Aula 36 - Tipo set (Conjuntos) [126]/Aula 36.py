"""
Class "set" - Conjuntos (baseado nos matemáticos) 
Representados graficamente pelo diagrama de Venn
Sets em Python são mutáveis, porém aceitam apenas tipos imutáveis como valor interno.

Sets são eficientes para remover valores duplicados de iteráveis.
- Não aceitam valores mutáveis; (list, dict)
- Seus valores serão sempre únicos: Eliminam valores duplicados
- Não tem índices;
- Não respeitam ordem na iteração;
- São iteráveis (for, in, not in)

Métodos úteis:
add, update, clear, discard

Operadores úteis:
união | união (union) - Une
intersecção & (intersection) - Itens presentes em ambos
diferença - Itens presentes apenas no set da esquerda
diferença simétrica ^ - Itens que não estão em ambos
"""

# Criando um set
s1 = set('Luiz')
s1 = set()  # vazio -> {} isso é um dict
s1 = {'Luiz', 1, 2, 3}  # com dados
# print(s1)

# Remove duplicatas
l1 = [1, 2, 3, 4, 5, 5, 5]
s2 = set(l1)  # Remove os 5 adicionais
# print(s2)

# Métodos
s3 = set()
s3.add("Gabriel")  # Só pode enviar um valor por vez
s3.update(("Hello world", 1, 2, 3, 4))  # Pode adicionar mais de um valor
# s3.clear()  # Limpa o set
s3.discard("Gabriel")  # Descarta um valor específico
# print(s3)

# Operadores
s4 = {1, 2, 3}
s5 = {2, 3, 4}
s6 = s4.union(s5)  # Une os dois sets
print(s6)  # {1, 2, 3, 4}

s6 = s4.intersection(s5)  # Guarda os valores em ambos os sets
print(s6)  # {2, 3}

s6 = s4.difference(s5)  # Retira os valores de um set do outro
print(s6)  # {1}

s6 = s4.symmetric_difference(s5)  # Pega os itens que não são comuns aos sets
print(s6)  # {1, 4}
