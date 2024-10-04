# Definição dos dados
n = 5  # tamanho da amostra
D = 3  # número de placas defeituosas no lote
N = 30  # tamanho total do lote

# Cálculo do valor esperado
E_X = n * (D / N)

# Cálculo da variância
# Fórmula: Var(X) = n * (D / N) * ((N - D) / N) * ((N - n) / (N - 1))
Var_X = n * (D / N) * ((N - D) / N) * ((N - n) / (N - 1))

# Resultados
print(f"Valor Esperado (E[X]): {E_X:.4f}")
print(f"Variância (Var[X]): {Var_X:.4f}")
