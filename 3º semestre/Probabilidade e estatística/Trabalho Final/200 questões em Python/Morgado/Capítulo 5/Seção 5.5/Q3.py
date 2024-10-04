from scipy.stats import binom

# Número de partidas
n = 10

# Probabilidade de A ganhar uma partida
p = 0.6

# Calcula a probabilidade de A ganhar a série (ou seja, mais de 5 partidas)
probabilidade = sum(binom.pmf(k, n, p) for k in range(6, 11))

print(f"A probabilidade de A ganhar a série é {probabilidade:.4f}")
