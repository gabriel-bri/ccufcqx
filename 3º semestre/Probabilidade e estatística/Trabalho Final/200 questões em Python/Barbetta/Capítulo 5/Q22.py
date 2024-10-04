import numpy as np
from scipy.stats import poisson, binom

# Taxa média de defeitos
lambda_defeitos = 0.05 * 6  # 0.05 defeitos/m² em uma área de 6 m²

# a) Probabilidade de não haver falhas
P_X_0 = poisson.pmf(0, lambda_defeitos)

# b) Probabilidade de haver mais de uma falha
P_X_1 = poisson.cdf(1, lambda_defeitos)
P_X_gt_1 = 1 - P_X_1

# c) Probabilidade de pelo menos 4 barcos não apresentarem defeito
# Probabilidade de um barco não ter falhas
p_no_falhas = P_X_0

# Usando a distribuição binomial
n_barcos = 5
k_minimo = 4
P_no_falhas_4 = binom.pmf(k_minimo, n_barcos, p_no_falhas)
P_no_falhas_5 = binom.pmf(n_barcos, n_barcos, p_no_falhas)
P_no_falhas_4_ou_mais = P_no_falhas_4 + P_no_falhas_5

# Resultados
print(f"Probabilidade de não haver falhas: {P_X_0:.4f}")
print(f"Probabilidade de haver mais de uma falha: {P_X_gt_1:.4f}")
print(f"Probabilidade de pelo menos 4 barcos não apresentarem defeito: {P_no_falhas_4_ou_mais:.4f}")
