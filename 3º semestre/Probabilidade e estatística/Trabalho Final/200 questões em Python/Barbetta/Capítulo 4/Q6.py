import math

# Valor de e
e = math.exp(1)

# a) Probabilidade de não ocorrer erro (k = 0)
P_0 = 1 / e

# b) Probabilidade de ocorrer mais do que dois erros (k > 2)
P_1 = 1 / e
P_2 = 1 / (2 * e)

P_maior_que_2 = 1 - (P_0 + P_1 + P_2)

# Forma alternativa: P(k > 2) = 1 - 5/2e
P_maior_que_2_alt = 1 - (5 / (2 * e))

# Resultados
print(f"Probabilidade de não ocorrer erro (k = 0): {P_0:.4f} ou 1/e")
print(f"Probabilidade de ocorrer mais do que dois erros (k > 2): {P_maior_que_2_alt:.4f} ou 1 - 5/2e")