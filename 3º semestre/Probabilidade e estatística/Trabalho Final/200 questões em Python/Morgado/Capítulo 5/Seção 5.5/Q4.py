from scipy.special import comb

# Probabilidade de A vencer uma partida
p = 0.4
q = 1 - p

# Número de partidas restantes
n = 13

# Calcula a probabilidade de A ganhar a série
probabilidade = 1 - sum(comb(n, k) * (p ** k) * (q ** (n - k)) for k in range(6))

print(f"A probabilidade de A ganhar a série é {probabilidade:.4f}")