from scipy.stats import norm

# distribuição de Poisson
lambda_ = 100
sigma = lambda_**0.5

# Correção de continuidade e cálculo do z-score
x = 120.5
mu = lambda_
z = (x - mu) / sigma

# Probabilidade de mais de 120 requisições
prob_more_than_120 = 1 - norm.cdf(z)

print(f"A probabilidade de ocorrerem mais de 120 requisições no próximo minuto é {prob_more_than_120:.4f}")
