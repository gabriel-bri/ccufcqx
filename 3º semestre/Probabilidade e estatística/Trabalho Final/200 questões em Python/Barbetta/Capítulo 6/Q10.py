from scipy.stats import norm
import numpy as np

mu_X = 1000  # Média
sigma_X = np.sqrt(10**2 + 4**2)  # Desvio padrão

# a) Probabilidade de o peso bruto ser superior a 1.020 g
x1 = 1020
z1 = (x1 - mu_X) / sigma_X
prob_a = 1 - norm.cdf(z1)

# b) Probabilidade do peso bruto estar entre 980 e 1.020 g
x2 = 980
z2 = (x2 - mu_X) / sigma_X
prob_b = norm.cdf(z1) - norm.cdf(z2)

print(f"a) A probabilidade de o peso bruto ser superior a 1.020 g é {prob_a:.4f}")
print(f"b) A probabilidade de o peso bruto estar entre 980 e 1.020 g é {prob_b:.4f}")
