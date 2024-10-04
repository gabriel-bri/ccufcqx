from scipy.stats import binom

# a) Exame com 10 questões
n_10 = 10
p = 1 / 4
k_min_10 = 5

# Probabilidade de obter pelo menos 5 acertos em 10 questões
prob_at_least_5_10 = 1 - binom.cdf(k_min_10 - 1, n_10, p)

# b) Exame com 100 questões
n_100 = 100
k_min_100 = 50

# Probabilidade de obter pelo menos 50 acertos em 100 questões
prob_at_least_50_100 = 1 - binom.cdf(k_min_100 - 1, n_100, p)

print(f"a) A probabilidade de aprovação em um exame com 10 questões é {prob_at_least_5_10:.4f}")
print(f"b) A probabilidade de aprovação em um exame com 100 questões é {prob_at_least_50_100:.4f}")
