import scipy.stats as stats

# Taxa média de chamadas por minuto
lambda_ = 5

# Número máximo de chamadas que a central pode processar
max_chamadas = 10

# Probabilidade de receber mais de 10 chamadas
# P(X > 10) = 1 - P(X <= 10)
probabilidade_menor_ou_igual_10 = stats.poisson.cdf(max_chamadas, lambda_)

# Probabilidade de receber mais de 10 chamadas
probabilidade_mais_de_10 = 1 - probabilidade_menor_ou_igual_10

# Resultados
print(f"Probabilidade de que a capacidade da central seja ultrapassada: {probabilidade_mais_de_10:.4f}")
