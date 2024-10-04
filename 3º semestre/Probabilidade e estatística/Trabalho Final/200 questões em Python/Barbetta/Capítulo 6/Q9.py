from scipy.stats import norm

# Parâmetros da distribuição normal
mu = 23
sigma = 4

# a) Probabilidade de o tempo de resposta ser menor do que 25 segundos
x1 = 25
prob_a = norm.cdf(x1, mu, sigma)

# b) Probabilidade de o tempo de resposta ficar entre 20 e 30 segundos
x2 = 20
x3 = 30
prob_b = norm.cdf(x3, mu, sigma) - norm.cdf(x2, mu, sigma)

# Imprimir os resultados
print(f"a) A probabilidade de o tempo de resposta ser menor do que 25 segundos é {prob_a:.4f}")
print(f"b) A probabilidade de o tempo de resposta ficar entre 20 e 30 segundos é {prob_b:.4f}")
