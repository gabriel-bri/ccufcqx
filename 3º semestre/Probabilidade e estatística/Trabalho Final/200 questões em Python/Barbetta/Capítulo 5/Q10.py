# Definindo os parâmetros
n = 5      # Tamanho da amostra
D = 3      # Número de placas defeituosas no lote
N = 30     # Tamanho total do lote

# Calculando o valor esperado
E_X = n * (D / N)

# Calculando a variância
Var_X = n * (D / N) * ((N - D) / N) * ((N - n) / (N - 1))

# Exibindo os resultados
print(f"Valor Esperado (E[X]): {E_X:.4f}")
print(f"Variância (Var[X]): {Var_X:.4f}")
