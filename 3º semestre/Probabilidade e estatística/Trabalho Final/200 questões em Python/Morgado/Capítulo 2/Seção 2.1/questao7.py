import math

num_elementos_A = 4
num_elementos_B = 7

# Número total de funções f: A -> B
total_funcoes = num_elementos_B ** num_elementos_A

# Número de funções injetoras f: A -> B
num_funcoes_injetoras = math.perm(num_elementos_B, num_elementos_A)

print("Número total de funções f: A -> B:", total_funcoes)
print("Número de funções injetoras f: A -> B:", num_funcoes_injetoras)
