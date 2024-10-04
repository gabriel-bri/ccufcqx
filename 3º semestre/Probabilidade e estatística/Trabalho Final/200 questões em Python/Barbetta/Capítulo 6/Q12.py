from scipy.stats import poisson

lambda_ = 70  # Média de solicitações em 10 minutos

# Probabilidade de ocorrer mais de 80 solicitações
prob_more_than_80 = 1 - poisson.cdf(80, lambda_)

# Imprimir o resultado
print(f"A probabilidade de ocorrer mais de 80 solicitações nos próximos 10 minutos é {prob_more_than_80:.4f}")
