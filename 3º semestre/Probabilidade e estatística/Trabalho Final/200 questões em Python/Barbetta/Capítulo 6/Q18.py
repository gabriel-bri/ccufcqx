from scipy.stats import norm, binom

mu = 320
sigma = 7

# a) Probabilidade de a tarefa ser executada entre 310 e 330 segundos
z_310 = (310 - mu) / sigma
z_330 = (330 - mu) / sigma
prob_310_330 = norm.cdf(z_330) - norm.cdf(z_310)

# b) Probabilidade de a tarefa demorar mais do que 325 segundos em pelo menos 50 vezes
x = 325
prob_more_than_325 = 1 - norm.cdf((x - mu) / sigma)

# Distribuição binomial
n = 200  # Número de execuções
k = 50   # Número de execuções onde a tarefa demora mais de 325 segundos

# 50 execuções demorarem mais de 325 segundos
prob_at_least_50 = 1 - binom.cdf(k - 1, n, prob_more_than_325)

print(f"a) A probabilidade de a tarefa ser executada entre 310 e 330 segundos é {prob_310_330:.4f}")
print(f"b) A probabilidade de a tarefa demorar mais do que 325 segundos em pelo menos 50 vezes em 200 execuções é {prob_at_least_50:.4f}")
