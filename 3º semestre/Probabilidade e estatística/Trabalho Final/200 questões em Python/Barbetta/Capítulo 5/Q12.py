import scipy.stats as stats
import numpy as np

# Dados fornecidos
p = 0.0002  # Probabilidade de erro em um único bit
n = 10000   # Número de bits transmitidos

# Taxa média de erros lambda
lambda_ = n * p

# Cálculo da probabilidade de ter mais de 4 erros
# P(X > 4) = 1 - P(X <= 4)
# P(X <= 4) é a soma das probabilidades de ter 0, 1, 2, 3 e 4 erros
probabilidade_menor_ou_igual_4 = stats.poisson.cdf(4, lambda_)

# Probabilidade de mais de 4 erros
probabilidade_mais_de_4 = 1 - probabilidade_menor_ou_igual_4

# Resultados
print(f"Probabilidade de que mais de quatro bits sejam recebidos com erro: {probabilidade_mais_de_4:.4f}")
