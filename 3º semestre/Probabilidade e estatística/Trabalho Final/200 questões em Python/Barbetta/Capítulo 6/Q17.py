from scipy.stats import norm, binom

# Dados da distribuição normal
mu = 75.4
sigma = 2.2

# a) Probabilidade de a temperatura ficar inferior a 70°C
x = 70
z = (x - mu) / sigma
prob_temp_below_70 = norm.cdf(z)

# Dados da distribuição binomial
n = 500  # Número de utilizações
p = prob_temp_below_70  # Probabilidade de a temperatura ser inferior a 70°C

# b) Probabilidade de mais de cinco falhas
k = 5
prob_more_than_5_failures = 1 - binom.cdf(k, n, p)

print(f"a) A probabilidade de a temperatura ficar inferior a 70°C é {prob_temp_below_70:.4f}")
print(f"b) A probabilidade de, em 500 utilizações, a temperatura não atingir 70°C mais de cinco vezes é {prob_more_than_5_failures:.4f}")
